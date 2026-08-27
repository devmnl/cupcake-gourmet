const API = 'https://cupcake-gourmet-wjam.onrender.com/api';

const STATUS = [
    { n: 1, t: 'Pedido recebido' },
    { n: 2, t: 'Em preparacao' },
    { n: 3, t: 'Saiu para entrega' },
    { n: 4, t: 'Entregue' }
];

function moeda(v) { return 'R$ ' + parseFloat(v).toFixed(2).replace('.', ','); }

function atualizarCont() {
    const c = JSON.parse(localStorage.getItem('carrinho') || '[]');
    const el = document.getElementById('contCarrinho');
    if (el) el.textContent = c.reduce((s, i) => s + i.quantity, 0);
}

function mostrarErro(m) {
    const el = document.getElementById('erroBusca');
    el.textContent = m;
    el.classList.remove('escondido');
}

function desenharStatus(atual) {
    const div = document.getElementById('stepper');
    div.innerHTML = STATUS.map(s => {
        let cls = 'status-etapa';
        if (s.n < atual) cls += ' feito';
        if (s.n === atual) cls += ' atual';
        return `<div class="${cls}">
            <div class="status-bola">${s.n < atual ? '✓' : s.n}</div>
            <div class="status-texto">${s.t}</div>
        </div>`;
    }).join('');
}

async function buscarPedido() {
    document.getElementById('erroBusca').classList.add('escondido');
    const id = parseInt(document.getElementById('idPedido').value);
    if (!id || id < 1) return mostrarErro('Informe um numero valido.');

    try {
        const r = await fetch(API + '/orders/' + id);
        if (!r.ok) {
            const d = await r.json().catch(() => ({}));
            return mostrarErro(d.error || 'Pedido nao encontrado.');
        }
        const p = await r.json();
        document.getElementById('rId').textContent = '#' + p.id;
        document.getElementById('rCliente').textContent = p.customer_name;
        document.getElementById('rTotal').textContent = moeda(p.total);
        document.getElementById('rPag').textContent = p.payment_method;
        document.getElementById('rData').textContent = new Date(p.created_at).toLocaleString('pt-BR');

        const obs = p.observation && p.observation.trim();
        const linhaObs = document.getElementById('linhaObs');
        if (obs) {
            document.getElementById('rObs').textContent = obs;
            linhaObs.classList.remove('escondido');
        } else {
            linhaObs.classList.add('escondido');
        }

        desenharStatus(p.status);

        document.getElementById('rItens').innerHTML = p.items.map(i =>
            `<div class="linha-detalhe">
                <span class="label-detalhe">${i.quantity}x ${i.name}</span>
                <span>${moeda(i.price * i.quantity)}</span>
            </div>`
        ).join('');

        document.getElementById('busca').classList.add('escondido');
        document.getElementById('resultado').classList.remove('escondido');
        window.scrollTo(0, 0);
    } catch (e) {
        mostrarErro('Erro ao consultar. O servidor esta rodando?');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    atualizarCont();
    const inp = document.getElementById('idPedido');
    if (inp) inp.addEventListener('keypress', e => { if (e.key === 'Enter') buscarPedido(); });
});
