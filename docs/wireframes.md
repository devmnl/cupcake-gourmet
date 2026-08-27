# Wireframes - Cupcake Gourmet

> Representação estrutural simplificada das telas implementadas.
> Os wireframes abaixo correspondem às páginas reais do sistema.

---

## 1. Página Inicial (index.html)

```
┌─────────────────────────────────────────────────────────┐
│  🧁 Cupcake Gourmet   Início  Produtos  🛒 Carrinho  ...│  <- Header com navegação
├─────────────────────────────────────────────────────────┤
│                                                         │
│              🍰 BEM-VINDO À CUPCAKE GOURMET!            │
│     Cupcakes artesanais feitos com ingredientes...      │
│                                                         │
│              [ IMAGEM / BANNER ]                        │
│                                                         │
│                  [ Ver Produtos >> ]                    │  <- Hero section
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│                   NOSSOS DESTAQUES                      │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  [IMG]   │  │  [IMG]   │  │  [IMG]   │              │
│  │ Cupcake  │  │ Cupcake  │  │ Cupcake  │  <- Cards    │
│  │ R$ 8,50  │  │ R$ 9,00  │  │ R$10,00  │     destaque│
│  │[Adicionar]│  │[Adicionar]│  │[Adicionar]│            │
│  └──────────┘  └──────────┘  └──────────┘              │
│                                                         │
│            [ Ver Todos os Produtos ]                    │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                      SOBRE NÓS                          │
│   Texto sobre a missão, qualidade e entrega da loja.    │
├─────────────────────────────────────────────────────────┤
│  © 2026 Cupcake Gourmet - Projeto Acadêmico PIT II      │  <- Footer
└─────────────────────────────────────────────────────────┘
```

---

## 2. Página de Produtos (produtos.html)

```
┌─────────────────────────────────────────────────────────┐
│  🧁 Cupcake Gourmet   Início  Produtos* 🛒 Carrinho  ...│
├─────────────────────────────────────────────────────────┤
│                                                         │
│                    NOSSO CARDÁPIO                       │
│   Escolha seus cupcakes favoritos e monte seu pedido!   │
│                                                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐       │
│  │   [IMAGEM]  │ │   [IMAGEM]  │ │   [IMAGEM]  │       │
│  │ [Chocolate] │ │ [Morango]   │ │ [Red Velvet]│       │
│  │ Cupcake...  │ │ Cupcake...  │ │ Cupcake...  │       │
│  │ R$ 8,50     │ │ R$ 9,00     │ │ R$10,00     │       │
│  │[+ Carrinho] │ │[+ Carrinho] │ │[+ Carrinho] │       │
│  └─────────────┘ └─────────────┘ └─────────────┘       │
│                                                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐       │
│  │   [IMAGEM]  │ │   [IMAGEM]  │ │   [IMAGEM]  │       │
│  │ [Baunilha]  │ │  [Nutella]  │ │   [Limão]   │       │
│  │ ...         │ │ ...         │ │ ...         │       │
│  │ R$ 7,50     │ │ R$11,00     │ │ R$ 8,00     │       │
│  │[+ Carrinho] │ │[+ Carrinho] │ │[+ Carrinho] │       │
│  └─────────────┘ └─────────────┘ └─────────────┘       │
│                                                         │
└─────────────────────────────────────────────────────────┘
  * Grid responsivo: 3 em desktop, 2 em tablet, 1 em mobile
```

---

## 3. Página do Carrinho (carrinho.html)

```
┌─────────────────────────────────────────────────────────┐
│  🧁 Cupcake Gourmet   ...  Carrinho*  ...              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│                     SEU CARRINHO                        │
│                                                         │
│  ┌─────────────────────────────────────────────────┐    │
│  │ [IMG] │ Cupcake de Chocolate                    │    │
│  │       │ R$ 8,50 cada                            │    │
│  │       │                    [-]  2  [+] R$17,00 🗑│    │  <- Item 1
│  ├─────────────────────────────────────────────────┤    │
│  │ [IMG] │ Cupcake de Morango                      │    │
│  │       │ R$ 9,00 cada                            │    │
│  │       │                    [-]  1  [+] R$ 9,00 🗑│    │  <- Item 2
│  ├─────────────────────────────────────────────────┤    │
│  │                                         Subtotal R$26,00│
│  │                                            Total R$26,00│ <- Destaque
│  ├─────────────────────────────────────────────────┤    │
│  │ [ Continuar Comprando ]    [ Finalizar Pedido ]│    │  <- Ações
│  └─────────────────────────────────────────────────┘    │
│                                                         │
│  (OU, se vazio:)                                         │
│             🛒 SEU CARRINHO ESTÁ VAZIO                   │
│             [ Ver Produtos ]                             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 4. Finalizar Pedido (finalizar.html)

```
┌─────────────────────────────────────────────────────────┐
│  ... Carrinho*  Finalizar                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│                 FINALIZAR PEDIDO                        │
│                                                         │
│  ┌─────────────────────────────────────────────────┐    │
│  │ RESUMO DO PEDIDO                                 │    │
│  │                        Total:         R$ 26,00  │    │
│  │                                                  │    │
│  │ DADOS DO CLIENTE                                 │    │
│  │  Nome Completo*    [________________________]    │    │
│  │  Telefone*        [ (00) 00000-0000         ]    │    │
│  │                                                  │    │
│  │ ENDEREÇO DE ENTREGA                              │    │
│  │  Endereço*        [________________________]    │    │
│  │  Número*   [____]  Bairro*  [______________]    │    │
│  │  Complemento (opcional)  [_________________]    │    │
│  │                                                  │    │
│  │ FORMA DE PAGAMENTO*                              │    │
│  │  [ Selecione... ▼ ]  (Pix / Dinheiro / Cartão)  │    │
│  │                                                  │    │
│  │      [  CONFIRMAR PEDIDO  ]  (botão destaque)   │    │
│  └─────────────────────────────────────────────────┘    │
│                                                         │
│  (OU, após sucesso:)                                    │
│  🎉 PEDIDO REALIZADO COM SUCESSO!                       │
│  Seu pedido foi confirmado. Número: [  #1  ]            │
│  [ Acompanhar Pedido ]  [ Continuar Comprando ]         │
└─────────────────────────────────────────────────────────┘
```

---

## 5. Acompanhar Pedido (acompanhar.html)

```
┌─────────────────────────────────────────────────────────┐
│  ... Acompanhar*                                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│                ACOMPANHAR PEDIDO                        │
│                                                         │
│  (Antes da busca:)                                      │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Informe o número do seu pedido:                  │    │
│  │  [  Nº do Pedido 🔍   ]   [ Buscar Pedido ]     │    │
│  └─────────────────────────────────────────────────┘    │
│                                                         │
│  (Após buscar com sucesso:)                             │
│  ┌─────────────────────────────────────────────────┐    │
│  │ DETALHES DO PEDIDO                               │    │
│  │  Pedido:          #1                             │    │
│  │  Cliente:         Cliente Teste                  │    │
│  │  Total:           R$ 26,00                       │    │
│  │  Pagamento:       Pix                            │    │
│  │  Data/Hora:       27/08/2026 14:30               │    │
│  │                                                   │    │
│  │ STATUS:                                           │    │
│  │  ① Pedido  ② Em  ③ Saiu  ④ Entregue             │    │
│  │  recebido prep. para ent.    (✓/circulos color.) │    │
│  │                                                   │    │
│  │ ITENS DO PEDIDO:                                  │    │
│  │  2x Cupcake de Chocolate           R$ 17,00     │    │
│  │  1x Cupcake de Morango             R$  9,00     │    │
│  │                                                   │    │
│  │             [ Nova Consulta ]                    │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

## 6. Área Administrativa (admin.html)

```
┌─────────────────────────────────────────────────────────┐
│  ... Admin*                                             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│              PAINEL ADMINISTRATIVO                      │
│                                                         │
│  ┌────────────────────────────────────────────────┐     │
│  │ [ Produtos ▾ ]  [ Pedidos ]    <- Abas/Tabs    │     │
│  ├────────────────────────────────────────────────┤     │
│  │                                                 │     │
│  │ ABA PRODUTOS:                                   │     │
│  │  Gerenciar Produtos         [+ Cadastrar]      │     │
│  │  ┌─────────────────────────────────────────┐   │     │
│  │  │ID│IMG│Nome     │Categoria│Preço│Ações  │   │     │
│  │  │1 │🧁 │Chocolate│Chocolate│R$8,50│[Ed][Ex]│   │     │
│  │  │2 │🧁 │Morango  │Frutas   │R$9,00│[Ed][Ex]│   │     │
│  │  │..│...│...      │...      │...   │...    │   │     │
│  │  └─────────────────────────────────────────┘   │     │
│  │                                                 │     │
│  │ (Modal Cadastrar/Editar:)                       │     │
│  │  Nome*        [_________________________]      │     │
│  │  Descrição*   [_________________________]      │     │
│  │  Preço* [___]  Categoria* [_____________]      │     │
│  │  URL Imagem*  [_________________________]      │     │
│  │              [Cancelar] [Salvar]               │     │
│  └────────────────────────────────────────────────┘     │
│                                                         │
│  (Ou ABA PEDIDOS:)                                      │
│  ┌─────────────────────────────────────────────────┐    │
│  │ID│Cliente  │Total  │Pagam.│Status     │Data│Ações│    │
│  │#1│Maria S. │R$26,00│Pix   │(3) Saiu..│..  │[V][S]│    │
│  │..│....     │...    │...   │...       │... │... │    │
│  └─────────────────────────────────────────────────┘    │
│                                                         │
│  (Modal Ver Pedido:)                                   │
│  Dados completos + itens + status badge.               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
