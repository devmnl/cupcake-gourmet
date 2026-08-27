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
| RNF02 | Navegação simples e intuitiva entre páginas | Alta |
| RNF03 | Mensagens de erro claras e compreensíveis | Alta |
| RNF04 | Pedidos armazenados permanentemente em banco SQLite | Alta |
| RNF05 | Compatibilidade com navegadores modernos (Chrome, Firefox, Edge, Safari) | Média |
| RNF06 | Carrinho armazenado no localStorage do navegador | Média |
| RNF07 | Comunicação via API REST JSON | Alta |
| RNF08 | Tempo de resposta da API < 2 segundos | Média |

## 3. Regras de Negócio

- RN01: O carrinho deve ter pelo menos 1 item para finalizar o pedido.
- RN02: O total do pedido é calculado multiplicando preço unitário por quantidade de cada item.
- RN03: O status do pedido segue a ordem: 1-Recebido → 2-Preparação → 3-Entrega → 4-Entregue.
- RN04: Preços de produtos devem ser valores positivos maiores que zero.
- RN05: Quantidades no carrinho devem ser valores inteiros maiores que zero.
- RN06: Todos os campos obrigatórios do formulário devem ser preenchidos.
- RN07: Telefone deve conter 11 dígitos (DDD + número).
