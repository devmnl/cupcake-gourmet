# Requisitos do Sistema - Cupcake Gourmet

## 1. Requisitos Funcionais (RF)

| ID | Descrição | Prioridade |
|---|---|---|
| RF01 | Visualizar cupcakes disponíveis no catálogo | Alta |
| RF02 | Adicionar produto ao carrinho de compras | Alta |
| RF03 | Alterar quantidade de produto no carrinho | Alta |
| RF04 | Remover produto do carrinho | Alta |
| RF05 | Calcular subtotal e total do pedido | Alta |
| RF06 | Finalizar pedido informando os dados do cliente | Alta |
| RF07 | Armazenar pedido no banco de dados SQLite | Alta |
| RF08 | Consultar o status do pedido por número | Alta |
| RF09 | Administrador visualizar os pedidos | Média |
| RF10 | Administrador alterar o status do pedido | Média |
| RF11 | Administrador cadastrar novo produto | Média |
| RF12 | Administrador editar produto existente | Média |
| RF13 | Administrador excluir produto | Média |
| RF14 | Pesquisar produtos pelo nome | Média |
| RF15 | Adicionar uma observação ao pedido | Média |

## 2. Requisitos Não Funcionais (RNF)

| ID | Descrição | Prioridade |
|---|---|---|
| RNF01 | Interface responsiva para computador, tablet e celular | Alta |
| RNF02 | Navegação simples entre as páginas | Alta |
| RNF03 | Mensagens de erro fáceis de entender | Alta |
| RNF04 | Pedidos salvos no banco SQLite | Alta |
| RNF05 | Funcionamento em navegadores modernos | Média |
| RNF06 | Carrinho armazenado no localStorage do navegador | Média |
| RNF07 | Comunicação entre front-end e back-end por API | Alta |

## 3. Regras de Negócio

- O carrinho precisa ter pelo menos 1 item para finalizar o pedido.
- O total é calculado pelo preço do produto multiplicado pela quantidade.
- O status do pedido segue a ordem: Recebido → Em preparação → Saiu para entrega → Entregue.
- Os preços dos produtos devem ser valores positivos.
- As quantidades dos produtos devem ser números inteiros positivos.
- Os campos obrigatórios do formulário precisam ser preenchidos.
- O telefone deve possuir 11 dígitos.
- A observação do pedido é opcional.
