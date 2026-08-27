# Wireframes - Cupcake Gourmet

Representação simples da estrutura das telas.

---

## 1. Página Inicial (index.html)

```
┌──────────────────────────────────────────────┐
│ 🧁 Cupcake Gourmet   Início  Produtos  Carrinho...  │ <- Cabeçalho / menu
├──────────────────────────────────────────────┤
│                                              │
│        🍰 BEM-VINDO À CUPCAKE GOURMET!       │
│   Cupcakes artesanais com ingredientes...    │
│                                              │
│           [ IMAGEM / BANNER ]                │
│                                              │
│               [ Ver Produtos ]               │ <- Botão principal
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│              NOSSOS DESTAQUES                │
│                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  [IMG]   │  │  [IMG]   │  │  [IMG]   │   │
│  │ Cupcake  │  │ Cupcake  │  │ Cupcake  │   │ <- 3 cards
│  │ R$ 8,50  │  │ R$ 9,00  │  │ R$10,00  │   │
│  │[Adicionar]│  │[Adicionar]│  │[Adicionar]│   │
│  └──────────┘  └──────────┘  └──────────┘   │
│                                              │
│       [ Ver Todos os Produtos ]              │
│                                              │
├──────────────────────────────────────────────┤
│ © 2026 Cupcake Gourmet - Projeto Acadêmico   │ <- Rodapé
└──────────────────────────────────────────────┘
```

---

## 2. Página de Produtos (produtos.html)

```
┌──────────────────────────────────────────────┐
│ ...     Produtos*    Carrinho  ...           │
├──────────────────────────────────────────────┤
│                                              │
│            NOSSO CARDÁPIO                    │
│  Escolha seus cupcakes e monte seu pedido!   │
│                                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │  [IMG]   │ │  [IMG]   │ │  [IMG]   │      │
│  │Chocolate │ │ Morango  │ │Red Velvet│      │
│  │ R$ 8,50  │ │ R$ 9,00  │ │ R$10,00  │      │
│  │[+Carrinho]│ │[+Carrinho]│ │[+Carrinho]│      │
│  └──────────┘ └──────────┘ └──────────┘      │
│                                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │ Baunilha │ │ Nutella  │ │  Limão   │      │
│  │ ...      │ │ ...      │ │ ...      │      │
│  └──────────┘ └──────────┘ └──────────┘      │
└──────────────────────────────────────────────┘
  * Grid responsivo: 3 desktop / 2 tablet / 1 mobile
```

---

## 3. Carrinho (carrinho.html)

```
┌──────────────────────────────────────────────┐
│ ...     Carrinho*    ...                     │
├──────────────────────────────────────────────┤
│                                              │
│              SEU CARRINHO                    │
│                                              │
│  ┌────────────────────────────────────────┐  │
│  │ [IMG]│ Cupcake de Chocolate             │  │
│  │      │ R$ 8,50 cada                     │  │
│  │      │              [-] 2 [+]  R$17,00 🗑│  │
│  ├────────────────────────────────────────┤  │
│  │ [IMG]│ Cupcake de Morango               │  │
│  │      │              [-] 1 [+]  R$ 9,00 🗑│  │
│  ├────────────────────────────────────────┤  │
│  │                           Subtotal R$26,00│  │
│  │                              Total R$26,00│  │
│  ├────────────────────────────────────────┤  │
│  │ [Continuar Comprando]  [Finalizar Pedido]│  │
│  └────────────────────────────────────────┘  │
│                                              │
│  (Se carrinho vazio:)                         │
│       🛒 CARRINHO VAZIO    [ Ver Produtos ]   │
└──────────────────────────────────────────────┘
```

---

## 4. Finalizar Pedido (finalizar.html)

```
┌──────────────────────────────────────────────┐
│ ... Carrinho  Finalizar*                     │
├──────────────────────────────────────────────┤
│                                              │
│           FINALIZAR PEDIDO                   │
│                                              │
│  ┌────────────────────────────────────────┐  │
│  │ RESUMO DO PEDIDO                        │  │
│  │                 Total:      R$ 26,00    │  │
│  │                                         │  │
│  │ DADOS DO CLIENTE                        │  │
│  │  Nome*       [____________________]     │  │
│  │  Telefone*   [ (00) 00000-0000     ]    │  │
│  │                                         │  │
│  │ ENDEREÇO                                │  │
│  │  Endereço*  [____________________]      │  │
│  │  Número* [___]  Bairro* [________]      │  │
│  │  Complemento (opcional) [_________]     │  │
│  │                                         │  │
│  │ PAGAMENTO*                              │  │
│  │  [ ▼ Selecione... ] (Pix/Dinheiro/Cartão)│  │
│  │                                         │  │
│  │      [ CONFIRMAR PEDIDO ]               │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  (Após sucesso:)                              │
│  🎉 PEDIDO REALIZADO!  Nº: #1                │
│  [ Acompanhar ]   [ Continuar Comprando ]    │
└──────────────────────────────────────────────┘
```

---

## 5. Acompanhar Pedido (acompanhar.html)

```
┌──────────────────────────────────────────────┐
│ ...    Acompanhar*                           │
├──────────────────────────────────────────────┤
│                                              │
│          ACOMPANHAR PEDIDO                   │
│                                              │
│  (Antes de buscar:)                          │
│  ┌────────────────────────────────────────┐  │
│  │ Informe o nº do pedido:                  │  │
│  │  [ Nº Pedido ]    [ Buscar Pedido ]      │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  (Depois de buscar:)                         │
│  ┌────────────────────────────────────────┐  │
│  │ DETALHES DO PEDIDO                      │  │
│  │  Pedido: #1   Cliente: Fulano...        │  │
│  │  Total: R$ 26,00   Pagamento: Pix       │  │
│  │  Data: 27/08/2026 14:30                 │  │
│  │                                         │  │
│  │ STATUS:                                 │  │
│  │  ① Recebido  ② Prepar.  ③ Saiu  ④ Entregue │
│  │                                         │  │
│  │ ITENS:                                  │  │
│  │  2x Cupcake de Chocolate  R$ 17,00      │  │
│  │  1x Cupcake de Morango    R$  9,00      │  │
│  │                                         │  │
│  │          [ Nova Consulta ]              │  │
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```

---

## 6. Área Administrativa (admin.html)

```
┌──────────────────────────────────────────────┐
│ ...     Admin*                               │
├──────────────────────────────────────────────┤
│                                              │
│        PAINEL ADMINISTRATIVO                 │
│                                              │
│  ┌────────────────────────────────────────┐  │
│  │ [ Produtos▾ ]  [ Pedidos ]   <- Abas    │  │
│  ├────────────────────────────────────────┤  │
│  │ ABA PRODUTOS:                           │  │
│  │ Gerenciar Produtos    [+ Cadastrar]     │  │
│  │ ┌─────────────────────────────────────┐ │  │
│  │ │ID│IMG│Nome  │Categoria│Preço│ Ações │ │  │
│  │ │1 │🧁 │Choc. │Chocolate│R$8,50│Ed/Ex │ │  │
│  │ │2 │🧁 │Mor.  │Frutas  │R$9,00│Ed/Ex │ │  │
│  │ └─────────────────────────────────────┘ │  │
│  │                                         │  │
│  │ (Modal de produto:)                     │  │
│  │  Nome: [______]  Descrição: [______]    │  │
│  │  Preço: [__]  Categoria: [______]       │  │
│  │  Imagem URL: [___________________]       │  │
│  │           [Cancelar]  [Salvar]          │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  (ABA PEDIDOS:)                               │
│  ┌────────────────────────────────────────┐  │
│  │ID│Cliente │Total  │Status      │Data│Ações│  │
│  │#1│Maria   │R$26,00│(3) Saiu...│..  │V/S  │  │
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```
