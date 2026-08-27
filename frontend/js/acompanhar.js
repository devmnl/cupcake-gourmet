const API_URL_ACOMPANHAR = 'http://localhost:5000/api';

const STATUS_LABELS = [
    { num: 1, label: 'Pedido recebido' },
    { num: 2, label: 'Em preparação' },
    { num: 3, label: 'Saiu para entrega' },
    { num: 4, label: 'Entregue' }
];

function formatCurrency(value) {
    return 'R$ ' + parseFloat(value).toFixed(2).replace('.', ',');
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    const total = cart.reduce((sum, item) => sum + item.quantity, 0);
    const countEl = document.getElementById('cartCount');
    if (countEl) countEl.textContent = total;
}

function showSearchError(message) {
    const errEl = document.getElementById('searchError');
    errEl.textContent = message;
    errEl.classList.remove('hidden');
}

function hideSearchError() {
    document.getElementById('searchError').classList.add('hidden');
}

function renderStatusTracker(currentStatus) {
    const tracker = document.getElementById('statusTracker');
    tracker.innerHTML = STATUS_LABELS.map(s => {
        let cls = 'status-step';
        if (s.num < currentStatus) cls += ' done';
        if (s.num === currentStatus) cls += ' active';
        return `
            <div class="${cls}">
                <div class="status-circle">
                    ${s.num < currentStatus ? '✓' : s.num}
                </div>
                <div class="status-text">${s.label}</div>
            </div>
        `;
    }).join('');
}

async function searchOrder() {
    hideSearchError();
    const orderIdInput = document.getElementById('orderId');
    const orderId = parseInt(orderIdInput.value);

    if (!orderId || orderId < 1) {
        showSearchError('Informe um número de pedido válido.');
        return;
    }

    try {
        const response = await fetch(`${API_URL_ACOMPANHAR}/orders/${orderId}`);
        if (!response.ok) {
            const data = await response.json().catch(() => ({}));
            showSearchError(data.error || 'Pedido não encontrado.');
            return;
        }

        const order = await response.json();

        document.getElementById('resOrderId').textContent = '#' + order.id;
        document.getElementById('resCustomer').textContent = order.customer_name;
        document.getElementById('resTotal').textContent = formatCurrency(order.total);
        document.getElementById('resPayment').textContent = order.payment_method;
        
        const date = new Date(order.created_at);
        document.getElementById('resDate').textContent = date.toLocaleString('pt-BR');

        renderStatusTracker(order.status);

        const itemsEl = document.getElementById('resItems');
        itemsEl.innerHTML = order.items.map(item => {
            const itemTotal = item.price * item.quantity;
            return `
                <div class="detail-row">
                    <span class="detail-label">
                        ${item.quantity}x ${item.name}
                    </span>
                    <span class="detail-value">${formatCurrency(itemTotal)}</span>
                </div>
            `;
        }).join('');

        document.getElementById('searchContainer').classList.add('hidden');
        document.getElementById('orderResult').classList.remove('hidden');
        window.scrollTo({ top: 0, behavior: 'smooth' });

    } catch (e) {
        showSearchError('Não foi possível consultar o pedido. Verifique se o servidor está rodando.');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();

    const input = document.getElementById('orderId');
    if (input) {
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') searchOrder();
        });
    }
});
