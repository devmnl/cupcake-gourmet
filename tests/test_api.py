import urllib.request
import json

BASE = 'http://localhost:5000/api'

def get(path):
    req = urllib.request.Request(BASE + path)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def post(path, data):
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(BASE + path, data=body, headers={'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read())

def put(path, data):
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(BASE + path, data=body, headers={'Content-Type': 'application/json'}, method='PUT')
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read())

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
        status, resp = post('/orders', pedido)
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
        status, resp = put(f'/orders/{pedido_id}/status', {'status': 3})
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
