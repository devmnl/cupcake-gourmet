# 🧁 Cupcake Gourmet

Projeto desenvolvido para a disciplina **Projeto Integrador Transdisciplinar II (PIT II)** do curso de Engenharia de Software.

## Sobre o projeto

O Cupcake Gourmet é um sistema web simples para uma loja de cupcakes. A ideia surgiu a partir da situação-problema trabalhada na PIT I, na qual foi proposta uma solução para ajudar uma loja a realizar seus pedidos pela internet.

Na PIT I foram realizados o levantamento dos requisitos, histórias de usuário, backlog, modelagem e prototipação. Nesta etapa, a proposta foi colocada em prática por meio do desenvolvimento do sistema.

O cliente pode visualizar os cupcakes, adicionar produtos ao carrinho, fazer um pedido e consultar o andamento da entrega. Também foi criada uma área simples para o administrador controlar os produtos e os pedidos.

## Objetivo

Desenvolver uma aplicação simples para colocar em prática os conhecimentos estudados durante o curso, principalmente na parte de desenvolvimento web, banco de dados e organização de requisitos.

## Tecnologias utilizadas

### Front-end

* HTML5
* CSS3
* JavaScript

### Back-end

* Python
* Flask

### Banco de dados

* SQLite

O JavaScript utiliza `fetch()` para enviar e receber informações da API criada com Flask. O carrinho utiliza `localStorage` para guardar os produtos temporariamente.

## Principais funcionalidades

### Cliente

* Visualizar a página inicial
* Visualizar os cupcakes disponíveis
* Buscar um produto pelo nome
* Adicionar produtos ao carrinho
* Alterar a quantidade dos produtos
* Remover produtos do carrinho
* Ver o valor total da compra
* Informar os dados para realizar o pedido
* Escolher a forma de pagamento
* Adicionar uma observação ao pedido
* Receber o número do pedido
* Consultar o status do pedido

### Administrador

* Visualizar produtos
* Cadastrar produtos
* Editar produtos
* Excluir produtos
* Visualizar pedidos
* Ver os detalhes dos pedidos
* Alterar o status dos pedidos

Os status utilizados são:

1. Pedido recebido
2. Em preparação
3. Saiu para entrega
4. Entregue

## Estrutura do projeto

```text
cupcake-gourmet/
│
├── frontend/
│   ├── index.html
│   ├── produtos.html
│   ├── carrinho.html
│   ├── finalizar.html
│   ├── acompanhar.html
│   ├── admin.html
│   ├── css/
│   └── js/
│
├── backend/
│   ├── app.py
│   └── cupcake.db
│
├── docs/
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
├── tests/
│   ├── test_api.py
│   └── test_unitario.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Banco de dados

Foi utilizado o **SQLite**, por ser um banco simples e adequado para o tamanho deste projeto.

O sistema utiliza três tabelas principais:

### products

Armazena os produtos da loja.

* id
* name
* description
* price
* category
* image

### orders

Armazena os pedidos realizados.

* id
* customer_name
* phone
* address
* number
* complement
* neighborhood
* payment_method
* observation
* total
* status
* created_at

### order_items

Armazena os produtos de cada pedido.

* id
* order_id
* product_id
* quantity
* price

## Como executar

### 1. Instalar o Python

É necessário ter o Python instalado no computador.

### 2. Instalar as dependências

Abra o terminal na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

### 3. Iniciar o sistema

Execute:

```bash
python backend/app.py
```

O Flask iniciará o servidor.

Depois acesse no navegador:

```text
http://localhost:5000
```

O banco de dados SQLite é criado automaticamente quando o sistema é iniciado pela primeira vez.

## Testes

Foram preparados dois conjuntos de testes para verificar o funcionamento do sistema:

### Testes unitários

Foi criado um teste unitário básico utilizando a biblioteca `unittest` do Python, que já vem instalada por padrão.

O arquivo [tests/test_unitario.py](file:///c:/Users/USER/Desktop/PIT/cupcake-gourmet/tests/test_unitario.py) possui **5 testes** para verificar o dicionário de status do pedido:

* status 1 = Pedido recebido
* status 2 = Em preparação
* status 3 = Saiu para entrega
* status 4 = Entregue
* quantidade total de status = 4

Para rodar os testes unitários, basta abrir o terminal na pasta do projeto e executar:

```bash
python -m unittest tests.test_unitario -v
```

### Testes de API (testes reais)

Também existe o arquivo `tests/test_api.py` com 4 testes básicos que se conectam diretamente à API (precisa do Flask rodando em `http://localhost:5000`).

### Testes com colegas

Existe também um arquivo específico em `docs/testes.md` para registrar os testes realizados com cinco colegas, conforme solicitado na PIT II. Os resultados serão preenchidos após a realização dos testes reais.

## Documentação

Os documentos utilizados no desenvolvimento do projeto estão na pasta `docs/`.

Nela estão os requisitos, histórias de usuário, backlog, metodologia, UML, wireframes, testes, laudo de qualidade, informações sobre hospedagem e roteiro da apresentação.

## Melhorias futuras

Algumas funcionalidades poderiam ser adicionadas em uma versão futura, como:

* login para administrador;
* pagamento online;
* notificações sobre o pedido;
* integração com serviços de entrega;
* testes mais completos.



## Considerações finais

O projeto foi desenvolvido como uma aplicação acadêmica para colocar em prática os conhecimentos trabalhados na PIT I e na PIT II.

A proposta foi utilizar tecnologias simples e desenvolver as principais funções necessárias para uma pequena loja de cupcakes realizar seus pedidos pela internet.

---

**Projeto:** Cupcake Gourmet — PIT II
**Curso:** Engenharia de Software
**Disciplina:** Projeto Integrador Transdisciplinar II

