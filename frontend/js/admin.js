const API_URL_ADMIN = 'http://localhost:5000/api';

const STATUS_OPTIONS = [
    { value: 1, label: 'Pedido recebido' },
    { value: 2, label: 'Em preparação' },
    { value: 3, label: 'Saiu para entrega' },
    { value: 4, label: 'Entregue' }
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

function switchTab(tab) {
    document.querySelectorAll('.admin-tab').forEach(t => t.classList.remove('active'));
    event.target.classList.add('active');

    document.getElementById('tabProducts').classList.add('hidden');
    document.getElementById('tabOrders').classList.add('hidden');

    if (tab === 'products') {
        document.getElementById('tabProducts').classList.remove('hidden');
        loadProductsAdmin();
    } else {
        document.getElementById('tabOrders').classList.remove('hidden');
        loadOrdersAdmin();
    }
}

async function loadProductsAdmin() {
    const tbody = document.getElementById('productsTable');
    try {
        const res = await fetch(`${API_URL_ADMIN}/products`);
        const products = await res.json();

        if (products.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:2rem; color:#8b7355;">Nenhum produto cadastrado.</td></tr>';
            return;
        }

        tbody.innerHTML = products.map(p => `
            <tr>
                <td>${p.id}</td>
                <td><img src="${p.image}" alt="${p.name}" style="width:50px; height:50px; border-radius:8px; object-fit:cover;" onerror="this.style.display='none'"></td>
                <td><strong>${p.name}</strong><br><small style="color:#8b7355;">${p.description.substring(0,60)}...</small></td>
                <td>${p.category}</td>
                <td style="font-weight:bold; color:#c44569;">${formatCurrency(p.price)}</td>
                <td>
                    <div class="table-actions">
                        <button class="btn btn-sm" onclick="editProduct(${p.id})">Editar</button>
                        <button class="btn btn-sm btn-danger" onclick="deleteProduct(${p.id})">Excluir</button>
                    </div>
                </td>
            </tr>
        `).join('');
    } catch (e) {
        tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; color:#c53030;">Erro ao carregar produtos.</td></tr>';
    }
}

async function loadOrdersAdmin() {
    const tbody = document.getElementById('ordersTable');
    try {
        const res = await fetch(`${API_URL_ADMIN}/orders`);
        const orders = await res.json();

        if (orders.length === 0) {
            tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:#8b7355;">Nenhum pedido cadastrado.</td></tr>';
            return;
        }

        tbody.innerHTML = orders.map(o => {
            const date = new Date(o.created_at);
            return `
                <tr>
                    <td><strong>#${o.id}</strong></td>
                    <td>${o.customer_name}</td>
                    <td style="font-weight:bold; color:#c44569;">${formatCurrency(o.total)}</td>
                    <td>${o.payment_method}</td>
                    <td><span class="status-badge status-${o.status}">${o.status_text}</span></td>
                    <td style="font-size:0.85rem;">${date.toLocaleDateString('pt-BR')} ${date.toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit'})}</td>
                    <td>
                        <div class="table-actions">
                            <button class="btn btn-sm" onclick="viewOrder(${o.id})">Ver</button>
                            <button class="btn btn-sm btn-secondary" onclick="changeStatus(${o.id}, ${o.status})">Status</button>
                        </div>
                    </td>
                </tr>
            `;
        }).join('');
    } catch (e) {
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; color:#c53030;">Erro ao carregar pedidos.</td></tr>';
    }
}

function openProductModal(productId = null) {
    const modal = document.getElementById('productModal');
    const form = document.getElementById('productForm');
    const title = document.getElementById('modalTitle');
    const submitBtn = document.getElementById('modalSubmitBtn');

    form.reset();
    document.getElementById('productId').value = '';

    if (productId) {
        title.textContent = 'Editar Produto';
        submitBtn.textContent = 'Atualizar';
        fetch(`${API_URL_ADMIN}/products/${productId}`)
            .then(r => r.json())
            .then(p => {
                document.getElementById('productId').value = p.id;
                document.getElementById('p_name').value = p.name;
                document.getElementById('p_description').value = p.description;
                document.getElementById('p_price').value = p.price;
                document.getElementById('p_category').value = p.category;
                document.getElementById('p_image').value = p.image;
            });
    } else {
        title.textContent = 'Cadastrar Produto';
        submitBtn.textContent = 'Cadastrar';
    }

    modal.classList.add('active');
}

function closeProductModal() {
    document.getElementById('productModal').classList.remove('active');
}

function editProduct(productId) {
    openProductModal(productId);
}

async function deleteProduct(productId) {
    if (!confirm('Tem certeza que deseja excluir este produto?')) return;

    try {
        const res = await fetch(`${API_URL_ADMIN}/products/${productId}`, { method: 'DELETE' });
        const data = await res.json();
        if (res.ok) {
            alert('Produto excluído com sucesso!');
            loadProductsAdmin();
        } else {
            alert(data.error || 'Erro ao excluir produto.');
        }
    } catch (e) {
        alert('Não foi possível excluir o produto.');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const productForm = document.getElementById('productForm');
    if (productForm) {
        productForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const id = document.getElementById('productId').value;
            const product = {
                name: document.getElementById('p_name').value.trim(),
                description: document.getElementById('p_description').value.trim(),
                price: parseFloat(document.getElementById('p_price').value),
                category: document.getElementById('p_category').value.trim(),
                image: document.getElementById('p_image').value.trim()
            };

            if (!product.name || !product.description || !product.price || !product.category || !product.image) {
                alert('Preencha todos os campos obrigatórios.');
                return;
            }
            if (product.price <= 0) {
                alert('Preço deve ser maior que zero.');
                return;
            }

            try {
                let res;
                if (id) {
                    res = await fetch(`${API_URL_ADMIN}/products/${id}`, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(product)
                    });
                } else {
                    res = await fetch(`${API_URL_ADMIN}/products`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(product)
                    });
                }

                const data = await res.json();
                if (res.ok) {
                    alert(data.message || 'Produto salvo com sucesso!');
                    closeProductModal();
                    loadProductsAdmin();
                } else {
                    alert(data.error || 'Erro ao salvar produto.');
                }
            } catch (e) {
                alert('Não foi possível salvar o produto. Verifique a conexão.');
            }
        });
    }
});

async function viewOrder(orderId) {
    try {
        const res = await fetch(`${API_URL_ADMIN}/orders/${orderId}`);
        if (!res.ok) {
            alert('Pedido não encontrado.');
            return;
        }
        const order = await res.json();
        const date = new Date(order.created_at);

        let itemsHtml = order.items.map(item => `
            <div class="detail-row">
                <span class="detail-label">${item.quantity}x ${item.name}</span>
                <span class="detail-value">${formatCurrency(item.price * item.quantity)}</span>
            </div>
        `).join('');

        document.getElementById('orderModalContent').innerHTML = `
            <div class="detail-row">
                <span class="detail-label">Pedido:</span>
                <span class="detail-value"><strong>#${order.id}</strong></span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Cliente:</span>
                <span class="detail-value">${order.customer_name}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Telefone:</span>
                <span class="detail-value">${order.phone}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Endereço:</span>
                <span class="detail-value">${order.address}, ${order.number}${order.complement ? ' - ' + order.complement : ''}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Bairro:</span>
                <span class="detail-value">${order.neighborhood}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Pagamento:</span>
                <span class="detail-value">${order.payment_method}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Status:</span>
                <span class="detail-value"><span class="status-badge status-${order.status}">${order.status_text}</span></span>
            </div>
            <div class="detail-row">
                <span class="detail-label">Data:</span>
                <span class="detail-value">${date.toLocaleString('pt-BR')}</span>
            </div>
            <h4 style="margin-top:1.5rem; margin-bottom:0.8rem; color:#c44569;">Itens do Pedido</h4>
            ${itemsHtml}
            <div class="detail-row" style="border-top: 2px solid #ffeef2; margin-top:1rem; padding-top:1rem;">
                <span class="detail-label" style="font-size:1.1rem;">TOTAL:</span>
                <span class="detail-value" style="font-weight:bold; color:#c44569; font-size:1.1rem;">${formatCurrency(order.total)}</span>
            </div>
            <div style="margin-top:1.5rem; text-align:right;">
                <button class="btn btn-secondary" onclick="closeOrderModal()">Fechar</button>
            </div>
        `;
        document.getElementById('orderModal').classList.add('active');
    } catch (e) {
        alert('Erro ao carregar detalhes do pedido.');
    }
}

function closeOrderModal() {
    document.getElementById('orderModal').classList.remove('active');
}

async function changeStatus(orderId, currentStatus) {
    const options = STATUS_OPTIONS.map(s =>
        `${s.value} - ${s.label}${s.value === currentStatus ? ' (atual)' : ''}`
    ).join('\n');

    const input = prompt(`Alterar status do pedido #${orderId}:\n\n${options}\n\nDigite o número do novo status (1-4):`, currentStatus);

    if (input === null) return;

    const newStatus = parseInt(input);
    if (![1, 2, 3, 4].includes(newStatus)) {
        alert('Status inválido. Digite um número entre 1 e 4.');
        return;
    }

    try {
        const res = await fetch(`${API_URL_ADMIN}/orders/${orderId}/status`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: newStatus })
        });
        const data = await res.json();
        if (res.ok) {
            alert('Status atualizado com sucesso!');
            loadOrdersAdmin();
        } else {
            alert(data.error || 'Erro ao atualizar status.');
        }
    } catch (e) {
        alert('Não foi possível atualizar o status.');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();
    loadProductsAdmin();
});
