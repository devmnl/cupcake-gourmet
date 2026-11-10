const API = 'https://cupcake-gourmet-wjam.onrender.com/api';
const TOKEN_CLIENTE = 'tokenCliente';

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

function escaparHtml(valor) {
    return String(valor ?? '').replace(/[&<>"']/g, caractere => ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
    })[caractere]);
}

function mostrarErroLogin(mensagem) {
    const el = document.getElementById('erroLogin');
    el.textContent = mensagem;
    el.classList.toggle('escondido', !mensagem);
}

function mostrarLogin() {
    document.getElementById('loginCliente').classList.remove('escondido');
    document.getElementById('painelCliente').classList.add('escondido');
    document.getElementById('resultado').classList.add('escondido');
}

async function requisicaoCliente(caminho, opcoes = {}) {
    const headers = { ...(opcoes.headers || {}) };
    const token = sessionStorage.getItem(TOKEN_CLIENTE);
    if (token) headers.Authorization = 'Bearer ' + token;
    const resposta = await fetch(API + caminho, { ...opcoes, headers });
    if (resposta.status === 401) encerrarSessao();
    return resposta;
}

async function abrirPainel(email) {
    document.getElementById('loginCliente').classList.add('escondido');
    document.getElementById('painelCliente').classList.remove('escondido');
    document.getElementById('resultado').classList.add('escondido');
    if (email) document.getElementById('clienteEmail').textContent = email;
    await carregarPedidos();
}

function encerrarSessao() {
    sessionStorage.removeItem(TOKEN_CLIENTE);
    document.getElementById('formLoginCliente').reset();
    document.getElementById('formCadastroCliente').reset();
    mostrarErroLogin('');
    mostrarLogin();
}

async function validarSessao() {
    if (!sessionStorage.getItem(TOKEN_CLIENTE)) {
        mostrarLogin();
        return;
    }

    try {
        const resposta = await requisicaoCliente('/customer/session');
        if (!resposta.ok) {
            encerrarSessao();
            return;
        }
        const cliente = await resposta.json();
        await abrirPainel(cliente.email);
    } catch (e) {
        mostrarLogin();
        mostrarErroLogin('Não foi possível conectar ao servidor. Tente novamente.');
    }
}

async function enviarCredenciais(caminho, dados, botao) {
    botao.disabled = true;
    mostrarErroLogin('');
    try {
        const resposta = await fetch(API + caminho, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        });
        const resultado = await resposta.json();
        if (!resposta.ok) {
            mostrarErroLogin(resultado.error || 'Não foi possível entrar.');
            return;
        }
        sessionStorage.setItem(TOKEN_CLIENTE, resultado.token);
        if (new URLSearchParams(window.location.search).get('retorno') === 'finalizar') {
            window.location.replace('finalizar.html');
            return;
        }
        await abrirPainel(resultado.email);
    } catch (e) {
        mostrarErroLogin('Não foi possível conectar ao servidor. Tente novamente.');
    } finally {
        botao.disabled = false;
    }
}

async function carregarPedidos() {
    const lista = document.getElementById('listaPedidos');
    const erro = document.getElementById('erroPedidos');
    erro.classList.add('escondido');
    lista.textContent = 'Carregando pedidos...';

    try {
        const resposta = await requisicaoCliente('/customer/orders');
        if (!resposta.ok) throw new Error('Não foi possível carregar seus pedidos.');
        const pedidos = await resposta.json();
        if (pedidos.length === 0) {
            lista.innerHTML = '<p>Você ainda não fez nenhum pedido. <a href="produtos.html">Ver produtos</a></p>';
            return;
        }
        lista.innerHTML = pedidos.map(pedido => `
            <div class="linha-detalhe">
                <span>
                    <strong>Pedido #${pedido.id}</strong> · ${escaparHtml(pedido.status_text)}
                    · ${moeda(pedido.total)}
                    · ${new Date(pedido.created_at).toLocaleDateString('pt-BR')}
                </span>
                <button class="btn btn-pequeno" type="button" data-pedido="${pedido.id}">Ver detalhes</button>
            </div>
        `).join('');
        lista.querySelectorAll('[data-pedido]').forEach(botao => {
            botao.addEventListener('click', () => abrirPedido(botao.dataset.pedido));
        });
    } catch (e) {
        lista.textContent = '';
        erro.textContent = e.message || 'Erro ao carregar seus pedidos.';
        erro.classList.remove('escondido');
    }
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

async function abrirPedido(id) {
    try {
        const r = await requisicaoCliente('/customer/orders/' + encodeURIComponent(id));
        if (!r.ok) throw new Error('Pedido não encontrado.');
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
                <span class="label-detalhe">${i.quantity}x ${escaparHtml(i.name)}</span>
                <span>${moeda(i.price * i.quantity)}</span>
            </div>`
        ).join('');

        document.getElementById('painelCliente').classList.add('escondido');
        document.getElementById('resultado').classList.remove('escondido');
        window.scrollTo(0, 0);
    } catch (e) {
        const erro = document.getElementById('erroPedidos');
        erro.textContent = e.message || 'Erro ao consultar pedido.';
        erro.classList.remove('escondido');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    atualizarCont();
    document.getElementById('formLoginCliente').addEventListener('submit', event => {
        event.preventDefault();
        enviarCredenciais('/customer/login', {
            email: document.getElementById('loginEmail').value,
            password: document.getElementById('loginSenha').value
        }, document.getElementById('loginSubmit'));
    });
    document.getElementById('formCadastroCliente').addEventListener('submit', event => {
        event.preventDefault();
        const senha = document.getElementById('cadastroSenha').value;
        if (senha !== document.getElementById('confirmarSenha').value) {
            mostrarErroLogin('As senhas não conferem.');
            return;
        }
        enviarCredenciais('/customer/register', {
            email: document.getElementById('cadastroEmail').value,
            password: senha
        }, document.getElementById('cadastroSubmit'));
    });
    document.getElementById('mostrarCadastro').addEventListener('click', () => {
        document.getElementById('formCadastroCliente').classList.remove('escondido');
        document.getElementById('mostrarCadastro').classList.add('escondido');
        mostrarErroLogin('');
    });
    document.getElementById('cancelarCadastro').addEventListener('click', () => {
        document.getElementById('formCadastroCliente').classList.add('escondido');
        document.getElementById('mostrarCadastro').classList.remove('escondido');
        mostrarErroLogin('');
    });
    document.getElementById('sairCliente').addEventListener('click', encerrarSessao);
    document.getElementById('voltarPedidos').addEventListener('click', () => {
        document.getElementById('resultado').classList.add('escondido');
        document.getElementById('painelCliente').classList.remove('escondido');
    });
    validarSessao();
});
