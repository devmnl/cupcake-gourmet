# 🧁 Cupcake Gourmet - PIT II

Sistema simples de vendas online para uma loja de cupcakes gourmet.  
Projeto acadêmico desenvolvido para a **PIT II (Projeto Integrador Transdisciplinar II)** do curso de Engenharia de Software.

---

## 📋 Descrição

O **Cupcake Gourmet** é uma aplicação web que permite ao cliente visualizar produtos, montar um carrinho de compras, finalizar pedidos e acompanhar o status de entrega. A área administrativa permite gerenciar o catálogo de produtos e alterar o andamento dos pedidos.

O projeto foi concebido na **PIT I** (por meio de levantamento de requisitos, histórias de usuário, backlog, wireframes e prototipação) e **implementado na PIT II** como um sistema funcional completo, simples e organizado.

---

## 🎯 Objetivo

Desenvolver uma aplicação **funcional, simples e acadêmicamente realista** para venda de cupcakes gourmet, melhorando a experiência do usuário nos processos de pedido, pagamento e entrega — e servindo como contraparte implementada de todo o planejamento da PIT I.

> Princípio de desenvolvimento:  
> **funcionar > ser simples > ser organizado > ser bonito**

---

## 🛠️ Tecnologias Utilizadas

**NÃO utilizamos React, Vue, Angular, Next.js, TypeScript, Vite, Node.js, npm, Bootstrap, Tailwind ou bibliotecas desnecessárias.**

### Front-end
- **HTML5** — Marcação semântica das páginas
- **CSS3** — Estilização visual com identidade de confeitaria (rosa, marrom, responsivo)
- **JavaScript Puro (ES6+)** — Interações, manipulação de DOM, carrinho em `localStorage` e requisições via `fetch()`

### Back-end
- **Python 3** — Linguagem de programação
- **Flask** — Microframework web para API REST
- **Flask-CORS** — Permite requisições entre frontend e backend em portas diferentes

### Banco de Dados
- **SQLite 3** — Banco relacional em arquivo (zero configuração)

### Comunicação
- **Fetch API** + **JSON** — Comunicação assíncrona entre frontend e API Flask

---

## ✨ Funcionalidades Principais

### Para o Cliente
- [x] Visualizar página inicial com apresentação e produtos em destaque
- [x] Visualizar catálogo completo de cupcakes (imagem, nome, descrição, categoria, preço)
- [x] Adicionar/remover produtos no carrinho
- [x] Alterar quantidades no carrinho
- [x] Calcular subtotal e total em tempo real
- [x] Finalizar pedido com dados do cliente e forma de pagamento (Pix / Dinheiro / Cartão)
- [x] Receber número do pedido após confirmação
- [x] Consultar status do pedido por número (4 etapas: Recebido → Preparação → Saiu para entrega → Entregue)
- [x] Interface 100% responsiva para celular, tablet e desktop

### Para o Administrador
- [x] Cadastrar novos produtos (nome, descrição, preço, categoria, imagem)
- [x] Editar produtos existentes
- [x] Excluir produtos
- [x] Listar todos os pedidos com dados resumidos
- [x] Visualizar detalhes completos de cada pedido (itens, endereço, pagamento)
- [x] Alterar status do pedido entre as 4 etapas

---

## 📁 Estrutura do Projeto

```
cupcake-gourmet/
├── frontend/                     # Aplicação web (abrir no navegador)
│   ├── index.html                # Página inicial
│   ├── produtos.html             # Catálogo de cupcakes
│   ├── carrinho.html             # Carrinho de compras
│   ├── finalizar.html            # Finalização do pedido
│   ├── acompanhar.html           # Consulta de status
│   ├── admin.html                # Painel administrativo
│   ├── css/
│   │   └── style.css             # Estilos visuais completos
│   └── js/
│       ├── produtos.js           # Carrega produtos via API
│       ├── carrinho.js           # Lógica do carrinho (localStorage)
│       ├── pedido.js             # Formulário e envio do pedido
│       ├── acompanhar.js         # Consulta por nº do pedido
│       └── admin.js              # CRUD de produtos e gestão de pedidos
│
├── backend/                      # Servidor Python/Flask
│   ├── app.py                    # API REST (endpoints Flask)
│   ├── database.py               # Criação das tabelas + seed inicial
│   └── cupcake.db                # Arquivo SQLite (gerado automaticamente)
│
├── docs/                         # 📚 Documentação acadêmica da PIT II
│   ├── requisitos.md             # RFs e RNFs
│   ├── historias-usuario.md      # Histórias com critérios de aceitação
│   ├── backlog.md                # Backlog + Sprints (Scrum adaptado)
│   ├── uml.md                    # Casos de uso + Diagrama de classes (Mermaid)
│   ├── wireframes.md             # Wireframes de todas as telas
│   ├── metodologia.md            # Scrum adaptado para projeto individual
│   ├── testes.md                 # Estrutura para 5 testes com colegas
│   ├── laudo-qualidade.md        # Modelo de laudo (problemas/correções)
│   ├── deploy.md                 # Como hospedar (PythonAnywhere, etc.)
│   ├── roteiro-video.md          # Roteiro do vídeo de ~5 minutos
│   └── evidencias/               # Pasta para prints e evidências
│
├── tests/
│   └── test_api.py               # 10 testes automatizados da API
│
├── requirements.txt              # Dependências Python (Flask + flask-cors)
├── .gitignore                    # Arquivos ignorados pelo Git
└── README.md                     # 👉 Este arquivo
```

---

## 🗄️ Banco de Dados (SQLite)

O banco de dados é automaticamente criado no primeiro acesso. Possui 3 tabelas relacionadas:

### Tabela: `products` (Produtos)
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | INTEGER PK | Identificador único |
| `name` | TEXT | Nome do cupcake |
| `description` | TEXT | Descrição detalhada |
| `price` | REAL | Preço unitário |
| `category` | TEXT | Categoria (ex: Chocolate, Frutas, etc.) |
| `image` | TEXT | URL da imagem do produto |

### Tabela: `orders` (Pedidos)
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | INTEGER PK | Número do pedido |
| `customer_name` | TEXT | Nome do cliente |
| `phone` | TEXT | Telefone para contato |
| `address` | TEXT | Rua / Avenida |
| `number` | TEXT | Número da casa/apt |
| `complement` | TEXT | Complemento (opcional) |
| `neighborhood` | TEXT | Bairro |
| `payment_method` | TEXT | Pix / Dinheiro / Cartão |
| `total` | REAL | Valor total do pedido |
| `status` | INTEGER | 1=Recebido, 2=Preparação, 3=Entrega, 4=Entregue |
| `created_at` | TIMESTAMP | Data/hora da criação |

### Tabela: `order_items` (Itens do Pedido)
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | INTEGER PK | Identificador do item |
| `order_id` | INTEGER FK | Referencia `orders.id` |
| `product_id` | INTEGER FK | Referencia `products.id` |
| `quantity` | INTEGER | Quantidade comprada |
| `price` | REAL | Preço unitário no momento da compra |

**Relacionamentos:**  
→ 1 pedido contém *muitos* itens (`orders 1 --- * order_items`)  
→ Cada item referencia *1* produto (`order_items * --- 1 products`)

---

## 🔌 API REST (Flask)

### Endpoints de Produtos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/products` | Lista todos os produtos |
| `GET` | `/api/products/<id>` | Retorna um produto por ID |
| `POST` | `/api/products` | Cadastra novo produto (JSON com name, description, price, category, image) |
| `PUT` | `/api/products/<id>` | Atualiza um produto existente |
| `DELETE` | `/api/products/<id>` | Remove um produto |

### Endpoints de Pedidos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/orders` | Lista todos os pedidos (ordenados por data) |
| `GET` | `/api/orders/<id>` | Consulta pedido completo (dados + itens) |
| `POST` | `/api/orders` | Cria novo pedido (JSON com dados do cliente + itens + total) |
| `PUT` | `/api/orders/<id>/status` | Altera status do pedido (1 a 4) |

Todas as respostas são em **JSON**.  
Em caso de erro: retorna `{"error": "mensagem"}` com o código HTTP apropriado.

---

## ▶️ Como Executar o Projeto

### Pré-requisitos
- Ter **Python 3.8+** instalado
- Navegador web moderno (Chrome, Edge, Firefox, Safari)

### Passo 1 — Instalar as dependências Python
Abra o terminal na **pasta raiz do projeto** (`cupcake-gourmet/`) e execute:

```bash
pip install -r requirements.txt
```

Isso instalará o **Flask** e o **flask-cors**.

### Passo 2 — Iniciar o servidor Backend
```bash
cd backend
python app.py
```

Você verá uma mensagem semelhante a:
```
 * Running on http://127.0.0.1:5000
```

O servidor Flask estará rodando em **http://localhost:5000** (modo debug ativado).  
As tabelas do SQLite serão criadas automaticamente e os 6 produtos iniciais serão inseridos.

### Passo 3 — Abrir o Frontend no navegador
Basta **duplo clique** no arquivo:
```
frontend/index.html
```

Ou, se preferir, acessar via navegador: `file:///caminho/para/projeto/frontend/index.html`

⚠️ **Importante:** Deixe o **backend rodando em segundo plano** enquanto usa o site — caso contrário, os produtos e pedidos não carregarão.

### Passo 4 — Rodar os testes automatizados (opcional)
Com o backend rodando, execute:
```bash
python tests/test_api.py
```

Serão executados **10 testes** cobrindo carregar produtos, CRUD, criar pedido, consultar, alterar status e calcular total.

---

## 🧪 Produtos Cadastrados Inicialmente

| ID | Nome | Categoria | Preço |
|----|------|-----------|-------|
| 1 | Cupcake de Chocolate | Chocolate | R$ 8,50 |
| 2 | Cupcake de Morango | Frutas | R$ 9,00 |
| 3 | Cupcake Red Velvet | Especiais | R$ 10,00 |
| 4 | Cupcake de Baunilha | Clássicos | R$ 7,50 |
| 5 | Cupcake de Nutella | Especiais | R$ 11,00 |
| 6 | Cupcake de Limão | Frutas | R$ 8,00 |

Gerencie-os na área administrativa: `frontend/admin.html`.

---

## 🔜 Melhorias Futuras (Não Implementadas)

Funcionalidades que podem ser adicionadas em versões posteriores do projeto:

- [ ] **Pagamento real** via integração com Mercado Pago, Stripe ou Pix
- [ ] **Autenticação de usuários** (login e senha para cliente e admin com hash)
- [ ] **Sistema de notificações** (e-mail e/ou WhatsApp ao mudar status do pedido)
- [ ] **Integração com sistema de entrega** (cálculo de frete por CEP, integração com motoboys)
- [ ] **Testes automatizados mais completos** (pytest + Selenium para frontend)
- [ ] **Integração Contínua / Entrega Contínua (CI/CD)** (GitHub Actions)
- [ ] **Migração para PostgreSQL** (se for subir para nuvem com disco volátil)
- [ ] **Avaliações e comentários** dos clientes sobre os produtos
- [ ] **Cupons de desconto** e promoções
- [ ] **Dashboard com gráficos** de vendas na área administrativa

---

## 📚 Documentação Acadêmica Completa

Tudo está dentro da pasta `docs/`:

| Arquivo | Conteúdo |
|---------|----------|
| `requisitos.md` | Requisitos funcionais e não funcionais |
| `historias-usuario.md` | 12 histórias de usuário com critérios de aceitação |
| `backlog.md` | Backlog completo + 4 Sprints planejadas |
| `uml.md` | Diagrama de casos de uso + classes (Mermaid) + sequência |
| `wireframes.md` | Wireframes textuais das 6 telas |
| `metodologia.md` | Scrum adaptado para projeto individual |
| `testes.md` | Estrutura para 5 testes com colegas (preencher depois) |
| `laudo-qualidade.md` | Laudo com registro de problemas/correções (preencher depois) |
| `deploy.md` | Passo a passo simplificado de hospedagem |
| `roteiro-video.md` | Roteiro para o vídeo de apresentação (~5 min) |
| `evidencias/` | Pasta preparada para prints, fotos e arquivos de evidência |

---

## 🎓 Informações Acadêmicas

- **Projeto:** Cupcake Gourmet — PIT II
- **Disciplina:** Projeto Integrador Transdisciplinar II
- **Curso:** Engenharia de Software
- **Período:** (Preencher posteriormente)
- **Instituição:** (Preencher posteriormente)
- **Autor:** (Preencher posteriormente)

---

## Git / GitHub

O projeto já está pronto para versionamento:

```bash
git init
git add .
git commit -m "Projeto PIT II - Cupcake Gourmet"
```

Adicione o remote do GitHub posteriormente:
```bash
git remote add origin https://github.com/SEU_USUARIO/cupcake-gourmet.git
git branch -M main
git push -u origin main
```

---

## Licença / Uso

Projeto de cunho **estritamente acadêmico**. Desenvolvido como atividade avaliativa do curso de Engenharia de Software.
