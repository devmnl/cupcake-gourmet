const API = 'https://cupcake-gourmet-wjam.onrender.com/api';

function moeda(v) { return 'R$ ' + parseFloat(v).toFixed(2).replace('.', ','); }

function atualizarCont() {
    const c = JSON.parse(localStorage.getItem('carrinho') || '[]');
    const t = c.reduce((s, i) => s + i.quantity, 0);
    const el = document.getElementById('contCarrinho');
    if (el) el.textContent = t;
}

function getCarrinho() { return JSON.parse(localStorage.getItem('carrinho') || '[]'); }
function salvarCarrinho(c) {
    localStorage.setItem('carrinho', JSON.stringify(c));
    atualizarCont();
}

function mudarQtd(id, delta) {
    const c = getCarrinho();
    const item = c.find(i => i.product_id === id);
    if (!item) return;
    item.quantity += delta;
    if (item.quantity <= 0) {
        if (!confirm('Remover item do carrinho?')) { item.quantity = 1; salvarCarrinho(c); render(); return; }
        salvarCarrinho(c.filter(i => i.product_id !== id));
    } else {
        salvarCarrinho(c);
    }
    render();
}

function removerItem(id) {
    if (!confirm('Remover item?')) return;
    salvarCarrinho(getCarrinho().filter(i => i.product_id !== id));
    render();
}

async function render() {
    const c = getCarrinho();
    const vazio = document.getElementById('vazio');
    const conteudo = document.getElementById('conteudo');
    const itensEl = document.getElementById('itens');
    const subEl = document.getElementById('subtotal');
    const totEl = document.getElementById('total');

    if (c.length === 0) {
        vazio.classList.remove('escondido');
        conteudo.classList.add('escondido');
        return;
    }
    vazio.classList.add('escondido');
    conteudo.classList.remove('escondido');

    let html = '';
    let subtotal = 0;
    for (const item of c) {
        try {
            const r = await fetch(API_C + '/products/' + item.product_id);
            if (!r.ok) continue;
            const p = await r.json();
            const totItem = p.price * item.quantity;
            subtotal += totItem;
            html += `
                <div class="item-carrinho">
                    <img src="${p.image}" class="item-img" alt="${p.name}">
                    <div>
                        <div class="item-nome">${p.name}</div>
                        <div style="font-size:12px; color:#8b7355;">${moeda(p.price)} cada</div>
                    </div>
                    <div class="qtd">
                        <button onclick="mudarQtd(${p.id}, -1)">-</button>
                        <span>${item.quantity}</span>
                        <button onclick="mudarQtd(${p.id}, 1)">+</button>
                    </div>
                    <div class="item-preco">${moeda(totItem)}</div>
                    <button class="item-remover" onclick="removerItem(${p.id})" title="Remover">🗑️</button>
                </div>
            `;
        } catch (e) {}
    }
    itensEl.innerHTML = html;
    subEl.textContent = moeda(subtotal);
    totEl.textContent = moeda(subtotal);
}

document.addEventListener('DOMContentLoaded', () => { atualizarCont(); render(); });
