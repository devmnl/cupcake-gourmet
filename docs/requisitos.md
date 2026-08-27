# Requisitos do Sistema - Cupcake Gourmet

## 1. Requisitos Funcionais (RF)

| ID | Descrição | Prioridade |
|----|-----------|------------|
| RF01 | Visualizar cupcakes disponíveis no catálogo | Alta |
| RF02 | Adicionar produto ao carrinho de compras | Alta |
| RF03 | Alterar quantidade de produto no carrinho | Alta |
| RF04 | Remover produto do carrinho | Alta |
| RF05 | Calcular subtotal e total do pedido | Alta |
| RF06 | Finalizar pedido informando dados do cliente | Alta |
| RF07 | Armazenar pedido no banco de dados SQLite | Alta |
| RF08 | Consultar status do pedido por número | Alta |
| RF09 | Administrador visualizar todos os pedidos | Média |
| RF10 | Administrador alterar status do pedido | Média |
| RF11 | Administrador cadastrar novo produto | Média |
| RF12 | Administrador editar produto existente | Média |
| RF13 | Administrador excluir produto | Média |

## 2. Requisitos Não Funcionais (RNF)

| ID | Descrição | Prioridade |
|----|-----------|------------|
| RNF01 | Interface responsiva (desktop, tablet, celular) | Alta |
| RNF02 | Navegação simples entre as páginas | Alta |
| RNF03 | Mensagens de erro fáceis de entender | Alta |
| RNF04 | Pedidos salvos permanentemente no SQLite | Alta |
| RNF05 | Funcionar em navegadores modernos (Chrome, Firefox, Edge) | Média |
| RNF06 | Carrinho salvo no localStorage do navegador | Média |
| RNF07 | Comunicação entre front e back-end por API REST JSON | Alta |

## 3. Regras de Negócio

- O carrinho precisa ter pelo menos 1 item para finalizar o pedido.
- O total é preço unitário × quantidade de cada item, somando todos.
- Status segue a ordem: 1-Recebido → 2-Preparação → 3-Saiu para entrega → 4-Entregue.
- Preços dos produtos são sempre valores positivos.
- Quantidades no carrinho são sempre números inteiros positivos.
- Campos obrigatórios do formulário de finalização precisam ser preenchidos.
- Telefone precisa ter 11 dígitos (DDD + número).
