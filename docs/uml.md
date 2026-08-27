# UML - Cupcake Gourmet

Este documento apresenta os principais diagramas UML utilizados no projeto para representar as funcionalidades do sistema e a estrutura básica dos dados.

## 1. Diagrama de Caso de Uso

O diagrama mostra as principais ações que podem ser realizadas pelo cliente e pelo administrador.

```mermaid
flowchart LR
    Cliente((Cliente))
    Admin((Administrador))

    Cliente --> P1[Visualizar produtos]
    Cliente --> P2[Realizar pedido]
    Cliente --> P3[Consultar pedido]

    Admin --> A1[Gerenciar produtos]
    Admin --> A2[Visualizar pedidos]
    Admin --> A3[Alterar status do pedido]
```

### Explicação

**Cliente**

O cliente pode visualizar os produtos disponíveis, realizar um pedido e consultar o andamento do pedido.

**Administrador**

O administrador pode gerenciar os produtos cadastrados, visualizar os pedidos realizados e alterar o status dos pedidos.

A opção de realizar pedido inclui as etapas de adicionar produtos ao carrinho, alterar quantidades, remover produtos e informar os dados da compra.

---

## 2. Diagrama de Classes

O diagrama apresenta as principais classes utilizadas para representar os produtos e pedidos do sistema.

```mermaid
classDiagram

    class Product {
        id
        name
        description
        price
        category
        image
    }

    class Order {
        id
        customer_name
        phone
        address
        number
        complement
        neighborhood
        payment_method
        observation
        total
        status
        created_at
    }

    class OrderItem {
        id
        order_id
        product_id
        quantity
        price
    }

    Order "1" --> "*" OrderItem : possui
    OrderItem "*" --> "1" Product : refere-se a
```

### Explicação das classes

| Classe        | Descrição                                           |
| ------------- | --------------------------------------------------- |
| **Product**   | Representa os cupcakes disponíveis para venda.      |
| **Order**     | Representa um pedido realizado pelo cliente.        |
| **OrderItem** | Representa cada produto que faz parte de um pedido. |

### Relacionamentos

* Um **Order** pode possuir vários **OrderItem**.
* Cada **OrderItem** está relacionado a um **Product**.
* Um produto pode aparecer em vários itens de pedidos diferentes.

## 3. Relação com o banco de dados

A modelagem foi feita de forma simples e está relacionada às tabelas utilizadas no banco SQLite:

* `Product` → `products`
* `Order` → `orders`
* `OrderItem` → `order_items`

Essa estrutura permite registrar os produtos da loja e os pedidos realizados pelos clientes.

## 4. Considerações

Os diagramas foram elaborados de acordo com as principais funcionalidades implementadas no sistema. A modelagem foi mantida simples para facilitar o desenvolvimento e a compreensão do projeto.

