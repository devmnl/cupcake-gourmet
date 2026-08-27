const API_URL_CARRINHO = 'http://localhost:5000/api';

function formatCurrency(value) {
    return 'R$ ' + parseFloat(value).toFixed(2).replace('.', ',');
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    const total = cart.reduce((sum, item) => sum + item.quantity, 0);
    const countEl = document.getElementById('cartCount');
    if (countEl) countEl.textContent = total;
}

function getCart() {
    return JSON.parse(localStorage.getItem('cart') || '[]');
}

function saveCart(cart) {
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
}

function updateQuantity(productId, delta) {
    const cart = getCart();
    const item = cart.find(i => i.product_id === productId);
    if (!item) return;

    item.quantity += delta;
    if (item.quantity <= 0) {
        const confirmRemove = confirm('Deseja remover este item do carrinho?');
        if (!confirmRemove) {
            item.quantity = 1;
            saveCart(cart);
            renderCart();
            return;
        }
        const newCart = cart.filter(i => i.product_id !== productId);
        saveCart(newCart);
    } else {
        saveCart(cart);
    }
    renderCart();
}

function removeItem(productId) {
    if (!confirm('Deseja remover este item do carrinho?')) return;
    const cart = getCart().filter(i => i.product_id !== productId);
    saveCart(cart);
    renderCart();
}

async function renderCart() {
    const cart = getCart();
    const emptyCart = document.getElementById('emptyCart');
    const cartContent = document.getElementById('cartContent');
    const cartItems = document.getElementById('cartItems');
    const subtotalEl = document.getElementById('subtotal');
    const totalEl = document.getElementById('total');

    if (cart.length === 0) {
        emptyCart.classList.remove('hidden');
        cartContent.classList.add('hidden');
        return;
    }

    emptyCart.classList.add('hidden');
    cartContent.classList.remove('hidden');

    let itemsHtml = '';
    let subtotal = 0;

    for (const item of cart) {
        const product = await fetch(`${API_URL_CARRINHO}/products/${item.product_id}`)
            .then(r => r.ok ? r.json() : null)
            .catch(() => null);

        if (!product) continue;

        const itemTotal = product.price * item.quantity;
        subtotal += itemTotal;

        itemsHtml += `
            <div class="cart-item">
                <img src="${product.image}" alt="${product.name}" class="cart-item-image" onerror="this.style.background='#ffeef2'; this.style.content='url(data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 80 80%22%3E%3Crect fill=%22%23ffeef2%22 width=%2280%22 height=%2280%22/%3E%3Ctext x=%2240%22 y=%2250%22 text-anchor=%22middle%22 font-size=%2240%22%3E🧁%3C/text%3E%3C/svg%3E)'">
                <div>
                    <div class="cart-item-name">${product.name}</div>
                    <div style="font-size: 0.85rem; color: #8b7355;">${formatCurrency(product.price)} cada</div>
                </div>
                <div class="qty-controls">
                    <button class="qty-btn" onclick="updateQuantity(${product.id}, -1)">-</button>
                    <span class="qty-value">${item.quantity}</span>
                    <button class="qty-btn" onclick="updateQuantity(${product.id}, 1)">+</button>
                </div>
                <div class="cart-item-price">${formatCurrency(itemTotal)}</div>
                <button class="remove-btn" title="Remover" onclick="removeItem(${product.id})">🗑️</button>
            </div>
        `;
    }

    cartItems.innerHTML = itemsHtml;
    subtotalEl.textContent = formatCurrency(subtotal);
    totalEl.textContent = formatCurrency(subtotal);
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();
    renderCart();
});
