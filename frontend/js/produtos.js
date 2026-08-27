const API = 'http://localhost:5000/api';
let listaProdutos = [];

function moeda(v) {
    return 'R$ ' + parseFloat(v).toFixed(2).replace('.', ',');
}

function atualizarContCarrinho() {
    const carrinho = JSON.parse(localStorage.getItem('carrinho') || '[]');
    const total = carrinho.reduce((s, i) => s + i.quantity, 0);
    const el = document.getElementById('contCarrinho');
    if (el) el.textContent = total;
}

function adicionarCarrinho(idProduto) {
    let carrinho = JSON.parse(localStorage.getItem('carrinho') || '[]');
    const jaExiste = carrinho.find(i => i.product_id === idProduto);
    if (jaExiste) {
        jaExiste.quantity += 1;
    } else {
        carrinho.push({ product_id: idProduto, quantity: 1 });
    }
    localStorage.setItem('carrinho', JSON.stringify(carrinho));
    atualizarContCarrinho();
    alert('Produto adicionado!');
}

function desenharProdutos(produtos) {
    const grid = document.getElementById('produtosGrid');
    if (!grid) return;
    if (produtos.length === 0) {
        grid.innerHTML = '<p style="text-align:center; grid-column:1/-1; color:#8b7355;">Nenhum produto encontrado.</p>';
        return;
    }
    grid.innerHTML = produtos.map(p => `
        <div class="produto-card">
            <img src="${p.image}" alt="${p.name}" class="produto-img">
            <div class="produto-info">
                <span class="produto-categoria">${p.category}</span>
                <div class="produto-nome">${p.name}</div>
                <p class="produto-desc">${p.description}</p>
                <div class="produto-preco">${moeda(p.price)}</div>
                <button class="btn btn-pequeno" onclick="adicionarCarrinho(${p.id})">Adicionar ao carrinho</button>
            </div>
        </div>
    `).join('');
}

function filtrarProdutos() {
    const termo = document.getElementById('buscaProduto')?.value.trim().toLowerCase() || '';
    if (!termo) return desenharProdutos(listaProdutos);
    const filtro = listaProdutos.filter(p => p.name.toLowerCase().includes(termo) || p.description.toLowerCase().includes(termo));
    desenharProdutos(filtro);
}

async function carregarProdutos() {
    const grid = document.getElementById('produtosGrid');
    if (!grid) return;
    try {
        const resp = await fetch(API + '/products');
        listaProdutos = await resp.json();
        desenharProdutos(listaProdutos);
    } catch (e) {
        grid.innerHTML = '<p style="text-align:center; grid-column:1/-1; color:#c53030;">Nao foi possivel carregar os produtos. O servidor esta rodando?</p>';
    }
}

async function carregarDestaques() {
    const div = document.getElementById('destaques');
    if (!div) return;
    try {
        const resp = await fetch(API + '/products');
        const produtos = (await resp.json()).slice(0, 3);
        div.innerHTML = produtos.map(p => `
            <div class="produto-card">
                <img src="${p.image}" class="produto-img" alt="${p.name}">
                <div class="produto-info">
                    <span class="produto-categoria">${p.category}</span>
                    <div class="produto-nome">${p.name}</div>
                    <div class="produto-preco">${moeda(p.price)}</div>
                    <button class="btn btn-pequeno" onclick="adicionarCarrinho(${p.id})">Adicionar</button>
                </div>
            </div>
        `).join('');
    } catch (e) {
        div.innerHTML = '<p style="color:#c53030; grid-column:1/-1; text-align:center;">Erro ao carregar destaques.</p>';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    atualizarContCarrinho();
    carregarProdutos();
    carregarDestaques();
});
