const API_URL_PEDIDO = 'http://localhost:5000/api';

function formatCurrency(value) {
    return 'R$ ' + parseFloat(value).toFixed(2).replace('.', ',');
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    const total = cart.reduce((sum, item) => sum + item.quantity, 0);
    const countEl = document.getElementById('cartCount');
    if (countEl) countEl.textContent = total;
}

function validatePhone(phone) {
    const cleaned = phone.replace(/\D/g, '');
    return cleaned.length === 11;
}

function applyPhoneMask(input) {
    let value = input.value.replace(/\D/g, '');
    if (value.length > 11) value = value.slice(0, 11);
    if (value.length > 6) {
        value = `(${value.slice(0,2)}) ${value.slice(2,7)}-${value.slice(7)}`;
    } else if (value.length > 2) {
        value = `(${value.slice(0,2)}) ${value.slice(2)}`;
    }
    input.value = value;
}

async function calculateTotal() {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    let total = 0;
    for (const item of cart) {
        try {
            const res = await fetch(`${API_URL_PEDIDO}/products/${item.product_id}`);
            if (res.ok) {
                const product = await res.json();
                total += product.price * item.quantity;
            }
        } catch (e) {}
    }
    return total;
}

function showError(message) {
    const errorEl = document.getElementById('errorMsg');
    errorEl.textContent = message;
    errorEl.classList.remove('hidden');
}

function hideError() {
    document.getElementById('errorMsg').classList.add('hidden');
}

async function loadSummary() {
    const total = await calculateTotal();
    const totalEl = document.getElementById('totalSummary');
    if (totalEl) totalEl.textContent = formatCurrency(total);
}

async function submitOrder(event) {
    event.preventDefault();
    hideError();

    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    if (cart.length === 0) {
        showError('Seu carrinho está vazio. Adicione produtos antes de finalizar.');
        return;
    }

    const customer_name = document.getElementById('customer_name').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const address = document.getElementById('address').value.trim();
    const number = document.getElementById('number').value.trim();
    const complement = document.getElementById('complement').value.trim();
    const neighborhood = document.getElementById('neighborhood').value.trim();
    const payment_method = document.getElementById('payment_method').value;

    if (!customer_name || !phone || !address || !number || !neighborhood || !payment_method) {
        showError('Preencha todos os campos obrigatórios.');
        return;
    }

    if (!validatePhone(phone)) {
        showError('Telefone inválido. Use o formato (00) 00000-0000.');
        return;
    }

    const items = [];
    let total = 0;
    for (const item of cart) {
        try {
            const res = await fetch(`${API_URL_PEDIDO}/products/${item.product_id}`);
            if (res.ok) {
                const product = await res.json();
                const price = product.price;
                total += price * item.quantity;
                items.push({
                    product_id: product.id,
                    quantity: item.quantity,
                    price: price
                });
            }
        } catch (e) {
            showError('Erro ao processar produtos do carrinho.');
            return;
        }
    }

    if (items.length === 0 || total <= 0) {
        showError('Erro ao calcular o total do pedido.');
        return;
    }

    const orderData = {
        customer_name,
        phone,
        address,
        number,
        complement,
        neighborhood,
        payment_method,
        total,
        items
    };

    try {
        const response = await fetch(`${API_URL_PEDIDO}/orders`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(orderData)
        });

        const data = await response.json();

        if (!response.ok) {
            showError(data.error || 'Não foi possível finalizar o pedido.');
            return;
        }

        document.getElementById('orderNumber').textContent = data.id;
        document.getElementById('formContainer').classList.add('hidden');
        document.getElementById('successContainer').classList.remove('hidden');
        localStorage.removeItem('cart');
        updateCartCount();
        window.scrollTo({ top: 0, behavior: 'smooth' });

    } catch (e) {
        showError('Não foi possível finalizar o pedido. Verifique se o servidor está rodando.');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();
    loadSummary();

    const phoneInput = document.getElementById('phone');
    if (phoneInput) {
        phoneInput.addEventListener('input', () => applyPhoneMask(phoneInput));
    }

    const form = document.getElementById('orderForm');
    if (form) {
        form.addEventListener('submit', submitOrder);
    }

    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    if (cart.length === 0) {
        const formContainer = document.getElementById('formContainer');
        if (formContainer) {
            formContainer.innerHTML = `
                <div class="empty-cart">
                    <div class="empty-cart-icon">🛒</div>
                    <h3>Seu carrinho está vazio</h3>
                    <p style="margin: 1rem 0;">Adicione produtos para finalizar o pedido.</p>
                    <a href="produtos.html" class="btn">Ver Produtos</a>
                </div>
            `;
        }
    }
});
