# Histórias de Usuário - Cupcake Gourmet

## Ator: Cliente

### HU-01: Visualizar cupcakes
> **Como** cliente  
> **Quero** visualizar os cupcakes disponíveis na loja  
> **Para** conhecer as opções e escolher meus produtos favoritos.

**Critérios de Aceitação:**
- A página de produtos exibe cards com imagem, nome, descrição, categoria e preço.
- Produtos são carregados dinamicamente via API.
- Em dispositivos móveis os cards se ajustam automaticamente.

---

### HU-02: Adicionar ao carrinho
> **Como** cliente  
> **Quero** adicionar cupcakes ao meu carrinho  
> **Para** montar meu pedido antes de finalizar a compra.

**Critérios de Aceitação:**
- Cada produto tem um botão "Adicionar ao carrinho".
- Ao clicar, o produto é salvo no localStorage.
- O contador do carrinho no menu é atualizado.
- Uma mensagem confirma a adição.

---

### HU-03: Alterar quantidade
> **Como** cliente  
> **Quero** aumentar ou diminuir a quantidade de cada item  
> **Para** ajustar meu pedido conforme minha necessidade.

**Critérios de Aceitação:**
- Botões + e - permitem alterar quantidade.
- Quantidade nunca fica menor que 1 ao decrementar (exceto se remover).
- Subtotal e total são recalculados automaticamente.

---

### HU-04: Remover produto
> **Como** cliente  
> **Quero** remover um produto do carrinho  
> **Para** retirar itens que não quero mais.

**Critérios de Aceitação:**
- Botão de remover disponível por item.
- Confirmação antes de excluir.
- Carrinho atualizado imediatamente.

---

### HU-05: Visualizar total
> **Como** cliente  
> **Quero** ver o subtotal e o total do meu pedido  
> **Para** saber exatamente quanto pagarei.

**Critérios de Aceitação:**
- Subtotal por item exibido.
- Total geral exibido em destaque.
- Valores formatados em R$.

---

### HU-06: Finalizar pedido
> **Como** cliente  
> **Quero** informar meus dados (nome, telefone, endereço, pagamento)  
> **Para** concluir meu pedido e receber os cupcakes.

**Critérios de Aceitação:**
- Formulário com todos os campos obrigatórios.
- Validação de telefone e campos vazios.
- Três opções de pagamento: Pix, Dinheiro, Cartão.
- Ao finalizar, o pedido é salvo no banco.
- Número do pedido é exibido em tela de sucesso.
- Carrinho é limpo automaticamente.

---

### HU-07: Consultar pedido
> **Como** cliente  
> **Quero** informar o número do meu pedido  
> **Para** acompanhar o status da entrega.

**Critérios de Aceitação:**
- Campo para digitar número do pedido.
- Exibe dados do cliente, total e status atual.
- Tracker visual com os 4 status: Recebido, Preparação, Saiu para entrega, Entregue.
- Lista todos os itens do pedido.
- Mensagem amigável se pedido não existir.

---

## Ator: Administrador

### HU-08: Cadastrar produto
> **Como** administrador  
> **Quero** cadastrar novos cupcakes  
> **Para** manter o catálogo sempre atualizado.

**Critérios de Aceitação:**
- Formulário com nome, descrição, preço, categoria, imagem.
- Validação de campos obrigatórios e preço positivo.
- Produto aparece imediatamente na lista.

---

### HU-09: Editar produto
> **Como** administrador  
> **Quero** editar informações de produtos existentes  
> **Para** corrigir dados ou atualizar preços.

**Critérios de Aceitação:**
- Botão "Editar" em cada linha da tabela.
- Modal carrega dados do produto selecionado.
- Após salvar, lista é atualizada.

---

### HU-10: Excluir produto
> **Como** administrador  
> **Quero** excluir produtos que não são mais vendidos  
> **Para** manter o catálogo organizado.

**Critérios de Aceitação:**
- Botão "Excluir" disponível.
- Confirmação antes de excluir.
- Produto removido da lista e do banco.

---

### HU-11: Visualizar pedidos
> **Como** administrador  
> **Quero** ver a lista de todos os pedidos  
> **Para** acompanhar as vendas da loja.

**Critérios de Aceitação:**
- Tabela com ID, cliente, total, pagamento, status e data.
- Badge colorido para cada status.
- Botão para ver detalhes completos.

---

### HU-12: Alterar status do pedido
> **Como** administrador  
> **Quero** atualizar o status do pedido  
> **Para** refletir o andamento real da produção e entrega.

**Critérios de Aceitação:**
- Botão "Status" em cada pedido.
- Opções de 1 a 4 com descrição.
- Status atual é indicado.
- Lista atualizada após alteração.
