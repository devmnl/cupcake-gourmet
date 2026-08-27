const API_URL = 'http://localhost:5000/api';

function formatCurrency(value) {
    return 'R$ ' + parseFloat(value).toFixed(2).replace('.', ',');
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    const total = cart.reduce((sum, item) => sum + item.quantity, 0);
    const countEl = document.getElementById('cartCount');
    if (countEl) countEl.textContent = total;
}

async function getProductById(productId) {
    try {
        const response = await fetch(`${API_URL}/products/${productId}`);
        if (!response.ok) return null;
        return await response.json();
    } catch (e) {
        return null;
    }
}

function addToCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart') || '[]');
    const existing = cart.find(item => item.product_id === productId);
    if (existing) {
        existing.quantity += 1;
    } else {
        cart.push({ product_id: productId, quantity: 1 });
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    alert('Produto adicionado ao carrinho!');
}

async function loadProducts() {
    const grid = document.getElementById('productsGrid');
    if (!grid) return;

    try {
        const response = await fetch(`${API_URL}/products`);
        if (!response.ok) {
            throw new Error('Erro na resposta da API');
        }
        const products = await response.json();

        if (products.length === 0) {
            grid.innerHTML = '<p style="text-align:center; grid-column:1/-1; color:#8b7355;">Nenhum produto cadastrado.</p>';
            return;
        }

        grid.innerHTML = products.map(p => `
            <div class="product-card">
                <img src="${p.image}" alt="${p.name}" class="product-image" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 200 200%22%3E%3Crect fill=%22%23ffeef2%22 width=%22200%22 height=%22200%22/%3E%3Ctext x=%22100%22 y=%22110%22 text-anchor=%22middle%22 font-size=%2260%22%3E🧁%3C/text%3E%3C/svg%3E'">
                <div class="product-info">
                    <span class="product-category">${p.category}</span>
                    <h4 class="product-name">${p.name}</h4>
                    <p class="product-description">${p.description}</p>
                    <p class="product-price">${formatCurrency(p.price)}</p>
                    <button class="btn btn-sm" onclick="addToCart(${p.id})">Adicionar ao carrinho</button>
                </div>
            </div>
        `).join('');
    } catch (e) {
        grid.innerHTML = '<p style="text-align:center; grid-column:1/-1; color:#c53030;">Não foi possível carregar os produtos. Verifique se o servidor está rodando.</p>';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();
    loadProducts();
});
