# Cupcake Gourmet - PIT II

Projeto acadêmico desenvolvido para a disciplina **Projeto Integrador Transdisciplinar II (PIT II)** do curso de Engenharia de Software.

O sistema é uma loja online simples de cupcakes, onde o cliente pode visualizar produtos, montar um carrinho, finalizar pedidos e acompanhar o status. Também possui uma área administrativa para gerenciar produtos e pedidos.

---

## Objetivo

Colocar em prática o planejamento realizado na PIT I, desenvolvendo um sistema web funcional que atenda aos requisitos levantados. O foco está no aprendizado das tecnologias básicas da web e na integração entre front-end, back-end e banco de dados.

---

## Tecnologias Utilizadas

O sistema foi desenvolvido utilizando tecnologias simples e amplamente ensinadas na faculdade:

### Front-end
- **HTML5** — estrutura das páginas
- **CSS3** — estilização visual com tema de cupcakes
- **JavaScript puro** — interações do usuário, carrinho em `localStorage` e requisições para a API

### Back-end
- **Python 3** — linguagem de programação
- **Flask** — microframework para criar a API REST
- **Flask-CORS** — permite a comunicação entre front e back-end

### Banco de Dados
- **SQLite** — banco em arquivo, sem necessidade de instalar servidor

*Não foram utilizados frameworks de front-end como React, Vue, Angular, nem TypeScript, Node.js, Bootstrap ou Tailwind.*

---

## Funcionalidades

### Para o Cliente
- Visualizar página inicial e produtos em destaque
- Visualizar catálogo completo de cupcakes
- Adicionar produtos ao carrinho
- Alterar quantidade ou remover itens do carrinho
- Visualizar subtotal e total
- Finalizar pedido preenchendo dados do cliente e escolhendo pagamento
- Receber o número do pedido após a compra
- Consultar o andamento do pedido por número

### Para o Administrador
- Visualizar lista de produtos
- Cadastrar novo produto
- Editar produto existente
- Excluir produto
- Visualizar todos os pedidos
- Alterar status do pedido (Recebido → Preparação → Saiu para entrega → Entregue)

---

## Estrutura Básica

```
cupcake-gourmet/
├── frontend/              # páginas do site (abrir no navegador)
│   ├── index.html         # página inicial
│   ├── produtos.html      # catálogo de cupcakes
│   ├── carrinho.html      # carrinho de compras
│   ├── finalizar.html     # finalização do pedido
│   ├── acompanhar.html    # consulta de status
│   ├── admin.html         # painel administrativo
│   ├── css/style.css      # estilos visuais
│   └── js/                # scripts JavaScript
│
├── backend/               # API Python + Flask
│   ├── app.py             # toda a API + criação do banco
│   └── cupcake.db         # arquivo SQLite (gerado automaticamente)
│
├── docs/                  # documentação acadêmica da PIT II
│   ├── requisitos.md
│   ├── historias-usuario.md
│   ├── backlog.md
│   ├── metodologia.md
│   ├── uml.md
│   ├── wireframes.md
│   ├── testes.md
│   ├── laudo-qualidade.md
│   ├── deploy.md
│   ├── roteiro-video.md
│   └── evidencias/
│
├── tests/test_api.py      # 4 testes básicos da API
├── requirements.txt       # dependências Python
└── README.md              # este arquivo
```

---

## Banco de Dados

O banco SQLite é criado automaticamente na primeira vez que o servidor roda, com 3 tabelas:

- **products**: id, name, description, price, category, image
- **orders**: id, customer_name, phone, address, number, complement, neighborhood, payment_method, total, status, created_at
- **order_items**: id, order_id, product_id, quantity, price

São cadastrados 6 cupcakes iniciais para demonstração (Chocolate, Morango, Red Velvet, Baunilha, Nutella e Limão).

---

## Como Executar

### 1. Instalar as dependências
Abra o terminal na pasta raiz do projeto e execute:
```
pip install -r requirements.txt
```

### 2. Iniciar o servidor back-end
```
cd backend
python app.py
```

O servidor ficará disponível em `http://localhost:5000`.

### 3. Abrir o site
Dê duplo clique no arquivo `frontend/index.html` para abrir no navegador.

> Importante: deixe o back-end rodando enquanto estiver usando o site.

### 4. Rodar os testes básicos (opcional)
Com o backend rodando:
```
python tests/test_api.py
```

---

## Melhorias Futuras

Algumas ideias para melhorar o projeto depois da entrega:
- Login e senha para o administrador
- Integração com pagamento real (Pix, cartão)
- Envio de e-mail ou WhatsApp com atualização do status
- Avaliações dos clientes nos produtos
- Cupons de desconto e promoções
- Gráficos de vendas na área administrativa

---

## Documentação

A documentação acadêmica completa está na pasta `docs/`, contendo requisitos, histórias de usuário, backlog, diagramas UML, wireframes, metodologia, estrutura para testes com colegas, laudo de qualidade, sugestões de deploy e roteiro do vídeo de apresentação.

---

Projeto de cunho acadêmico, desenvolvido para a disciplina PIT II de Engenharia de Software.
