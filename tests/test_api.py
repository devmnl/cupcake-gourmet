import urllib.request
import json
import os
import uuid

BASE = 'http://localhost:5000/api'
TOKEN_CLIENTE = None

def get(path, token=None):
    headers = {}
    if token or (TOKEN_CLIENTE and (path.startswith('/orders/') or path.startswith('/customer/'))):
        headers['Authorization'] = 'Bearer ' + (token or TOKEN_CLIENTE)
    req = urllib.request.Request(BASE + path, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def post(path, data, token=None):
    body = json.dumps(data).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    req = urllib.request.Request(BASE + path, data=body, headers=headers, method='POST')
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read())

def put(path, data, token=None):
    body = json.dumps(data).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    req = urllib.request.Request(BASE + path, data=body, headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read())

def login_admin():
    usuario = os.environ.get('ADMIN_USERNAME')
    senha = os.environ.get('ADMIN_PASSWORD')
    if not usuario or not senha:
        raise RuntimeError('Configure ADMIN_USERNAME e ADMIN_PASSWORD para testar o painel.')
    body = json.dumps({'username': usuario, 'password': senha}).encode('utf-8')
    req = urllib.request.Request(
        BASE + '/admin/login',
        data=body,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())['token']

def registrar_cliente():
    global TOKEN_CLIENTE
    email = f'teste-{uuid.uuid4().hex}@exemplo.com'
    status, resposta = post('/customer/register', {
        'email': email,
        'password': 'senha-teste-segura'
    })
    if status != 201:
        raise RuntimeError(f'Nao foi possivel cadastrar cliente de teste: {resposta}')
    TOKEN_CLIENTE = resposta['token']

ok = 0
falhou = 0

def passou(msg):
    global ok
    ok += 1
    print(f'[OK] {msg}')

def falhar(msg):
    global falhou
    falhou += 1
    print(f'[FALHOU] {msg}')

print('=' * 50)
print('TESTE 1: Listar produtos (GET /api/products)')
print('=' * 50)
try:
    produtos = get('/products')
    if isinstance(produtos, list) and len(produtos) > 0:
        passou(f'{len(produtos)} produtos encontrados. Ex: "{produtos[0]["name"]}"')
    else:
        falhar('Nenhum produto retornado.')
except Exception as e:
    falhar(f'Erro: {e}')

print()
print('=' * 50)
print('TESTE 2: Criar pedido (POST /api/orders)')
print('=' * 50)
pedido_id = None
try:
    produtos = get('/products')
    if len(produtos) == 0:
        falhar('Sem produtos para criar pedido.')
    else:
        registrar_cliente()
        itens = [
            {'product_id': produtos[0]['id'], 'quantity': 2, 'price': produtos[0]['price']},
            {'product_id': produtos[-1]['id'], 'quantity': 1, 'price': produtos[-1]['price']}
        ]
        total = sum(i['quantity'] * i['price'] for i in itens)
        pedido = {
            'customer_name': 'Aluno Teste',
            'phone': '(11) 98765-4321',
            'address': 'Rua da Universidade',
            'number': '100',
            'complement': '',
            'neighborhood': 'Centro',
            'payment_method': 'Dinheiro',
            'observation': 'Entregar sem cobertura de morango.',
            'total': total,
            'items': itens
        }
        status, resp = post('/orders', pedido, TOKEN_CLIENTE)
        if status == 200 or status == 201:
            pedido_id = resp['id']
            passou(f'Pedido #{pedido_id} criado. Total: R$ {total:.2f}')
        else:
            falhar(f'Status {status}.')
except Exception as e:
    falhar(f'Erro: {e}')

print()
print('=' * 50)
print('TESTE 3: Consultar pedido (GET /api/orders/<id>)')
print('=' * 50)
try:
    if not pedido_id:
        falhar('Pedido não criado no teste anterior.')
    else:
        p = get(f'/orders/{pedido_id}')
        if p['id'] == pedido_id and 'items' in p and p['customer_name'] == 'Aluno Teste' and 'Entregar sem cobertura' in p.get('observation', ''):
            passou(f'Pedido #{p["id"]} consultado. Cliente: {p["customer_name"]}, Itens: {len(p["items"])}, Observacao: {p["observation"]}, Status: {p["status_text"]}')
        else:
            falhar('Dados do pedido não conferem (faltando observation?).')
except Exception as e:
    falhar(f'Erro: {e}')

print()
print('=' * 50)
print('TESTE 4: Alterar status do pedido (PUT /api/orders/<id>/status)')
print('=' * 50)
try:
    if not pedido_id:
        falhar('Pedido não criado.')
    else:
        token = login_admin()
        status, resp = put(f'/orders/{pedido_id}/status', {'status': 3}, token)
        if status == 200:
            p = get(f'/orders/{pedido_id}')
            if p['status'] == 3:
                passou(f'Status alterado para "{p["status_text"]}".')
            else:
                falhar(f'Status esperado 3, recebido {p["status"]}')
        else:
            falhar(f'Status HTTP {status}.')
except Exception as e:
    falhar(f'Erro: {e}')

print()
print('=' * 50)
print(f'RESULTADO: {ok} aprovados, {falhou} falhos.')
print('=' * 50)
if falhou == 0:
    print('Todos os testes basicos passaram.')
else:
    print('Atencao: houve falhas nos testes.')
    exit(1)
