const API_P = 'https://cupcake-gourmet-wjam.onrender.com/api';

function moeda(v) { return 'R$ ' + parseFloat(v).toFixed(2).replace('.', ','); }

function atualizarCont() {
    const c = JSON.parse(localStorage.getItem('carrinho') || '[]');
    const el = document.getElementById('contCarrinho');
    if (el) el.textContent = c.reduce((s, i) => s + i.quantity, 0);
}

function mascaraTel(input) {
    let v = input.value.replace(/\D/g, '').slice(0, 11);
    if (v.length > 6) v = `(${v.slice(0,2)}) ${v.slice(2,7)}-${v.slice(7)}`;
    else if (v.length > 2) v = `(${v.slice(0,2)}) ${v.slice(2)}`;
    input.value = v;
}

function telValido(t) { return t.replace(/\D/g, '').length === 11; }

async function calcTotal() {
    const c = JSON.parse(localStorage.getItem('carrinho') || '[]');
    let total = 0;
    for (const i of c) {
        try {
            const r = await fetch(API_P + '/products/' + i.product_id);
            if (r.ok) {
                const p = await r.json();
                total += p.price * i.quantity;
            }
        } catch (e) {}
    }
    return total;
}

function erro(msg) {
    const el = document.getElementById('erroMsg');
    el.textContent = msg;
    el.classList.remove('escondido');
}

async function carregarTotal() {
    const t = await calcTotal();
    const el = document.getElementById('totalResumo');
    if (el) el.textContent = moeda(t);
}

async function enviarPedido(e) {
    e.preventDefault();
    document.getElementById('erroMsg').classList.add('escondido');
    const c = JSON.parse(localStorage.getItem('carrinho') || '[]');
    if (c.length === 0) return erro('Carrinho vazio!');

    const nome = document.getElementById('customer_name').value.trim();
    const tel  = document.getElementById('phone').value.trim();
    const end  = document.getElementById('address').value.trim();
    const num  = document.getElementById('number').value.trim();
    const bai  = document.getElementById('neighborhood').value.trim();
    const pg   = document.getElementById('payment_method').value;
    const comp = document.getElementById('complement').value.trim();
    const obs  = document.getElementById('observation').value.trim();

    if (!nome || !tel || !end || !num || !bai || !pg) return erro('Preencha todos os campos obrigatorios.');
    if (!telValido(tel)) return erro('Telefone invalido.');

    const itens = [];
    let total = 0;
    for (const i of c) {
        try {
            const r = await fetch(API_P + '/products/' + i.product_id);
            if (r.ok) {
                const p = await r.json();
                total += p.price * i.quantity;
                itens.push({ product_id: p.id, quantity: i.quantity, price: p.price });
            }
        } catch (e) { return erro('Erro ao processar produtos.'); }
    }
    if (itens.length === 0) return erro('Erro no carrinho.');

    try {
        const r = await fetch(API_P + '/orders', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                customer_name: nome, phone: tel, address: end, number: num,
                complement: comp, neighborhood: bai, payment_method: pg,
                observation: obs, total: total, items: itens
            })
        });
        const d = await r.json();
        if (!r.ok) return erro(d.error || 'Erro ao finalizar.');

        document.getElementById('numPedido').textContent = d.id;
        document.getElementById('formContainer').classList.add('escondido');
        document.getElementById('sucessoContainer').classList.remove('escondido');
        localStorage.removeItem('carrinho');
        atualizarCont();
        window.scrollTo(0, 0);
    } catch (e) {
        erro('Nao foi possivel finalizar. O servidor esta rodando?');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    atualizarCont();
    carregarTotal();
    const tel = document.getElementById('phone');
    if (tel) tel.addEventListener('input', () => mascaraTel(tel));

    const form = document.getElementById('formPedido');
    if (form) form.addEventListener('submit', enviarPedido);

    const c = JSON.parse(localStorage.getItem('carrinho') || '[]');
    if (c.length === 0 && document.getElementById('formContainer')) {
        document.getElementById('formContainer').innerHTML = `
            <div class="carrinho-vazio">
                <div class="icone">🛒</div>
                <h3>Carrinho vazio</h3>
                <p style="margin:12px 0;">Adicione produtos para finalizar.</p>
                <a href="produtos.html" class="btn">Ver Produtos</a>
            </div>`;
    }
});
