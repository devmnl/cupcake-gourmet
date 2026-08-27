const API_ADM = 'https://cupcake-gourmet-wjam.onrender.com/api';

function moeda(v) { return 'R$ ' + parseFloat(v).toFixed(2).replace('.', ','); }

function atualizarCont() {
    const c = JSON.parse(localStorage.getItem('carrinho') || '[]');
    const el = document.getElementById('contCarrinho');
    if (el) el.textContent = c.reduce((s, i) => s + i.quantity, 0);
}

function trocarAba(aba) {
    document.querySelectorAll('.admin-aba').forEach(b => b.classList.remove('ativa'));
    event.target.classList.add('ativa');
    document.getElementById('abaProdutos').classList.add('escondido');
    document.getElementById('abaPedidos').classList.add('escondido');
    if (aba === 'produtos') {
        document.getElementById('abaProdutos').classList.remove('escondido');
        carregarProdutos();
    } else {
        document.getElementById('abaPedidos').classList.remove('escondido');
        carregarPedidos();
    }
}

async function carregarProdutos() {
    const tb = document.getElementById('tbProdutos');
    try {
        const r = await fetch(API_ADM + '/products');
        const lista = await r.json();
        if (lista.length === 0) {
            tb.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:20px;">Nenhum produto.</td></tr>';
            return;
        }
        tb.innerHTML = lista.map(p => `
            <tr>
                <td>${p.id}</td>
                <td><img src="${p.image}" style="width:45px; height:45px; border-radius:5px; object-fit:cover;"></td>
                <td><strong>${p.name}</strong><br><small style="color:#8b7355;">${p.description.slice(0, 50)}...</small></td>
                <td>${p.category}</td>
                <td><strong style="color:#c44569;">${moeda(p.price)}</strong></td>
                <td>
                    <div class="tabela-acoes">
                        <button class="btn btn-pequeno" onclick="editarProduto(${p.id})">Editar</button>
                        <button class="btn btn-pequeno btn-perigo" onclick="excluirProduto(${p.id})">Excluir</button>
                    </div>
                </td>
            </tr>`
        ).join('');
    } catch (e) {
        tb.innerHTML = '<tr><td colspan="6" style="text-align:center; color:#c53030;">Erro ao carregar.</td></tr>';
    }
}

async function carregarPedidos() {
    const tb = document.getElementById('tbPedidos');
    try {
        const r = await fetch(API_ADM + '/orders');
        const lista = await r.json();
        if (lista.length === 0) {
            tb.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:20px;">Nenhum pedido.</td></tr>';
            return;
        }
        tb.innerHTML = lista.map(o => {
            const d = new Date(o.created_at);
            return `<tr>
                <td><strong>#${o.id}</strong></td>
                <td>${o.customer_name}</td>
                <td><strong style="color:#c44569;">${moeda(o.total)}</strong></td>
                <td>${o.payment_method}</td>
                <td><span class="status-tag status-${o.status}">${o.status_text}</span></td>
                <td style="font-size:12px;">${d.toLocaleDateString('pt-BR')} ${d.toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit'})}</td>
                <td>
                    <div class="tabela-acoes">
                        <button class="btn btn-pequeno" onclick="verPedido(${o.id})">Ver</button>
                        <button class="btn btn-pequeno btn-secundario" onclick="mudarStatus(${o.id})">Status</button>
                    </div>
                </td>
            </tr>`;
        }).join('');
    } catch (e) {
        tb.innerHTML = '<tr><td colspan="7" style="text-align:center; color:#c53030;">Erro ao carregar.</td></tr>';
    }
}

function abrirModalProduto(id) {
    document.getElementById('formProduto').reset();
    document.getElementById('pId').value = '';
    document.getElementById('modalTitulo').textContent = id ? 'Editar Produto' : 'Cadastrar Produto';
    document.getElementById('modalSubmit').textContent = id ? 'Atualizar' : 'Cadastrar';
    if (id) {
        fetch(API_ADM + '/products/' + id).then(r => r.json()).then(p => {
            document.getElementById('pId').value = p.id;
            document.getElementById('pNome').value = p.name;
            document.getElementById('pDesc').value = p.description;
            document.getElementById('pPreco').value = p.price;
            document.getElementById('pCat').value = p.category;
            document.getElementById('pImg').value = p.image;
        });
    }
    document.getElementById('modalProduto').classList.add('ativo');
}

function fecharModalProduto() { document.getElementById('modalProduto').classList.remove('ativo'); }

function editarProduto(id) { abrirModalProduto(id); }

async function excluirProduto(id) {
    if (!confirm('Excluir produto?')) return;
    try {
        const r = await fetch(API_ADM + '/products/' + id, { method: 'DELETE' });
        const d = await r.json();
        alert(r.ok ? d.message : d.error);
        if (r.ok) carregarProdutos();
    } catch (e) { alert('Erro de conexao.'); }
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formProduto');
    if (form) form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const id = document.getElementById('pId').value;
        const dados = {
            name: document.getElementById('pNome').value.trim(),
            description: document.getElementById('pDesc').value.trim(),
            price: parseFloat(document.getElementById('pPreco').value),
            category: document.getElementById('pCat').value.trim(),
            image: document.getElementById('pImg').value.trim()
        };
        if (!dados.name || !dados.description || !dados.price || !dados.category || !dados.image)
            return alert('Preencha todos os campos.');
        if (dados.price <= 0) return alert('Preco invalido.');

        try {
            const url = id ? API_ADM + '/products/' + id : API_ADM + '/products';
            const metodo = id ? 'PUT' : 'POST';
            const r = await fetch(url, {
                method: metodo,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(dados)
            });
            const d = await r.json();
            alert(r.ok ? d.message : d.error);
            if (r.ok) { fecharModalProduto(); carregarProdutos(); }
        } catch (e) { alert('Erro de conexao.'); }
    });

    atualizarCont();
    carregarProdutos();
});

async function verPedido(id) {
    try {
        const r = await fetch(API_ADM + '/orders/' + id);
        if (!r.ok) return alert('Pedido nao encontrado.');
        const o = await r.json();
        const d = new Date(o.created_at);
        document.getElementById('modalConteudoPedido').innerHTML = `
            <div class="linha-detalhe"><span class="label-detalhe">Pedido:</span> <strong>#${o.id}</strong></div>
            <div class="linha-detalhe"><span class="label-detalhe">Cliente:</span> ${o.customer_name}</div>
            <div class="linha-detalhe"><span class="label-detalhe">Telefone:</span> ${o.phone}</div>
            <div class="linha-detalhe"><span class="label-detalhe">Endereco:</span> ${o.address}, ${o.number}${o.complement ? ' - ' + o.complement : ''}</div>
            <div class="linha-detalhe"><span class="label-detalhe">Bairro:</span> ${o.neighborhood}</div>
            <div class="linha-detalhe"><span class="label-detalhe">Pagamento:</span> ${o.payment_method}</div>
            ${o.observation && o.observation.trim() ? `<div class="linha-detalhe"><span class="label-detalhe">Observação:</span> ${o.observation}</div>` : ''}
            <div class="linha-detalhe"><span class="label-detalhe">Status:</span> <span class="status-tag status-${o.status}">${o.status_text}</span></div>
            <div class="linha-detalhe"><span class="label-detalhe">Data:</span> ${d.toLocaleString('pt-BR')}</div>
            <h4 style="margin-top:15px; margin-bottom:8px; color:#c44569;">Itens</h4>
            ${o.items.map(i =>
                `<div class="linha-detalhe">
                    <span class="label-detalhe">${i.quantity}x ${i.name}</span>
                    <span>${moeda(i.price * i.quantity)}</span>
                </div>`
            ).join('')}
            <div class="linha-detalhe" style="border-top:2px solid #ffeef2; margin-top:10px; padding-top:10px;">
                <span class="label-detalhe" style="font-size:16px;">TOTAL:</span>
                <strong style="color:#c44569; font-size:16px;">${moeda(o.total)}</strong>
            </div>
            <div style="text-align:right; margin-top:15px;">
                <button class="btn btn-secundario" onclick="fecharModalPedido()">Fechar</button>
            </div>`;
        document.getElementById('modalPedido').classList.add('ativo');
    } catch (e) { alert('Erro ao carregar pedido.'); }
}

function fecharModalPedido() { document.getElementById('modalPedido').classList.remove('ativo'); }

async function mudarStatus(id) {
    const s = prompt('Alterar status (1-Recebido, 2-Preparacao, 3-Entrega, 4-Entregue):\nDigite o novo numero (1-4):');
    if (s === null) return;
    const num = parseInt(s);
    if (![1,2,3,4].includes(num)) return alert('Status invalido.');
    try {
        const r = await fetch(API_ADM + '/orders/' + id + '/status', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: num })
        });
        const d = await r.json();
        alert(r.ok ? d.message : d.error);
        if (r.ok) carregarPedidos();
    } catch (e) { alert('Erro de conexao.'); }
}
