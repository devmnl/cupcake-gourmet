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

def delete(path):
    req = urllib.request.Request(BASE + path, method='DELETE')
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read())

print('=' * 60)
print('TESTE 1: Carregar produtos (GET /api/products)')
print('=' * 60)
products = get('/products')
print(f'OK - {len(products)} produtos carregados:')
for p in products[:3]:
    print(f'  #{p["id"]} {p["name"]} - R$ {p["price"]}')

print()
print('=' * 60)
print('TESTE 2: Carregar produto por ID (GET /api/products/1)')
print('=' * 60)
p1 = get('/products/1')
print(f'OK - Produto #{p1["id"]}: {p1["name"]}')

print()
print('=' * 60)
print('TESTE 3: Cadastrar produto (POST /api/products)')
print('=' * 60)
novo_produto = {
    'name': 'Cupcake Teste',
    'description': 'Produto criado para teste automatizado.',
    'price': 5.50,
    'category': 'Teste',
    'image': 'https://example.com/teste.jpg'
}
status, resp = post('/products', novo_produto)
novo_id = resp['id']
print(f'OK - Produto #{novo_id} cadastrado: {resp["message"]}')

print()
print('=' * 60)
print('TESTE 4: Editar produto (PUT /api/products/<id>)')
print('=' * 60)
novo_produto['name'] = 'Cupcake Teste Editado'
novo_produto['price'] = 6.90
status, resp = put(f'/products/{novo_id}', novo_produto)
print(f'OK - {resp["message"]}')

atualizado = get(f'/products/{novo_id}')
assert atualizado['name'] == 'Cupcake Teste Editado'
assert atualizado['price'] == 6.90
print(f'OK - Validação: nome = "{atualizado["name"]}", preço = R$ {atualizado["price"]}')

print()
print('=' * 60)
print('TESTE 5: Excluir produto (DELETE /api/products/<id>)')
print('=' * 60)
status, resp = delete(f'/products/{novo_id}')
print(f'OK - {resp["message"]}')
products_apos = get('/products')
ids_existentes = [p['id'] for p in products_apos]
assert novo_id not in ids_existentes
print('OK - Produto não existe mais na lista.')

print()
print('=' * 60)
print('TESTE 6: Criar pedido (POST /api/orders)')
print('=' * 60)
products = get('/products')
itens_pedido = [
    {'product_id': products[0]['id'], 'quantity': 2, 'price': products[0]['price']},
    {'product_id': products[1]['id'], 'quantity': 1, 'price': products[1]['price']}
]
total_esperado = sum(i['quantity'] * i['price'] for i in itens_pedido)
pedido = {
    'customer_name': 'Cliente Teste',
    'phone': '(11) 99999-9999',
    'address': 'Rua das Flores',
    'number': '123',
    'complement': 'Apto 45',
    'neighborhood': 'Centro',
    'payment_method': 'Pix',
    'total': total_esperado,
    'items': itens_pedido
}
status, resp = post('/orders', pedido)
pedido_id = resp['id']
print(f'OK - Pedido #{pedido_id} criado. Total = R$ {total_esperado:.2f}. Mensagem: {resp["message"]}')

print()
print('=' * 60)
print('TESTE 7: Consultar pedido (GET /api/orders/<id>)')
print('=' * 60)
pedido_consultado = get(f'/orders/{pedido_id}')
print(f'OK - Pedido #{pedido_consultado["id"]}')
print(f'  Cliente: {pedido_consultado["customer_name"]}')
print(f'  Total: R$ {pedido_consultado["total"]}')
print(f'  Status ({pedido_consultado["status"]}): {pedido_consultado["status_text"]}')
print(f'  Itens: {len(pedido_consultado["items"])} item(ns)')
assert len(pedido_consultado['items']) == 2
assert pedido_consultado['total'] == total_esperado
print('OK - Validações: total e quantidade de itens corretos.')

print()
print('=' * 60)
print('TESTE 8: Listar todos os pedidos (GET /api/orders)')
print('=' * 60)
orders = get('/orders')
print(f'OK - {len(orders)} pedido(s) listados.')

print()
print('=' * 60)
print('TESTE 9: Alterar status do pedido (PUT /api/orders/<id>/status)')
print('=' * 60)
status, resp = put(f'/orders/{pedido_id}/status', {'status': 3})
print(f'OK - {resp["message"]}')
pedido_status = get(f'/orders/{pedido_id}')
assert pedido_status['status'] == 3
assert pedido_status['status_text'] == 'Saiu para entrega'
print(f'OK - Status atual: ({pedido_status["status"]}) {pedido_status["status_text"]}')

print()
print('=' * 60)
print('TESTE 10: Calcular total do pedido (cálculo interno)')
print('=' * 60)
calculado = sum(i['price'] * i['quantity'] for i in pedido_consultado['items'])
print(f'Soma dos itens: R$ {calculado:.2f}')
print(f'Total do pedido: R$ {pedido_consultado["total"]:.2f}')
assert abs(calculado - pedido_consultado['total']) < 0.01
print('OK - Cálculo do total confere com a soma dos itens.')

print()
print('=' * 60)
print('🎉 TODOS OS TESTES FORAM APROVADOS! 🎉')
print('=' * 60)
