import json
import urllib.request
import uuid

BASE = 'http://localhost:5000/api'
TOKEN_CLIENTE = None


def get(path, token=None):
    headers = {}
    if token or TOKEN_CLIENTE:
        headers['Authorization'] = 'Bearer ' + (token or TOKEN_CLIENTE)
    req = urllib.request.Request(BASE + path, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def post(path, data, token=None):
    body = json.dumps(data).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    req = urllib.request.Request(
        BASE + path,
        data=body,
        headers=headers,
        method='POST'
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read())


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
print('TESTE 2: Criar pedido autenticado (POST /api/orders)')
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
        status, resposta = post('/orders', pedido, TOKEN_CLIENTE)
        if status == 201:
            pedido_id = resposta['id']
            passou(f'Pedido #{pedido_id} criado. Total: R$ {total:.2f}')
        else:
            falhar(f'Status {status}.')
except Exception as e:
    falhar(f'Erro: {e}')

print()
print('=' * 50)
print('TESTE 3: Consultar pedido proprio (GET /api/customer/orders/<id>)')
print('=' * 50)
try:
    if not pedido_id:
        falhar('Pedido não criado no teste anterior.')
    else:
        pedido = get(f'/customer/orders/{pedido_id}')
        if (
            pedido['id'] == pedido_id
            and 'items' in pedido
            and pedido['customer_name'] == 'Aluno Teste'
            and 'Entregar sem cobertura' in pedido.get('observation', '')
        ):
            passou(f'Pedido #{pedido["id"]} consultado para o cliente autenticado.')
        else:
            falhar('Os dados do pedido não conferem.')
except Exception as e:
    falhar(f'Erro: {e}')

print()
print('=' * 50)
print('TESTE 4: Listar histórico próprio (GET /api/customer/orders)')
print('=' * 50)
try:
    pedidos = get('/customer/orders')
    if any(pedido['id'] == pedido_id for pedido in pedidos):
        passou(f'Pedido #{pedido_id} aparece no histórico do cliente.')
    else:
        falhar(f'Pedido #{pedido_id} não apareceu no histórico do cliente.')
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
