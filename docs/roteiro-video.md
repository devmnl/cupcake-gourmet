# Roteiro do Vídeo de Apresentação - Cupcake Gourmet

> Preparado para aproximadamente **5 minutos**.
> Pontos de fala organizados em ordem de exibição.
> O vídeo NÃO será gerado aqui — este é apenas o roteiro textual.

---

## ⏱️ Duração Total Estimada: ~5 minutos

---

### 🎬 Parte 1: Abertura e Situação-Problema (~30 segundos)

**Cena:** Tela inicial do projeto, apresentador cumprimenta.

> "Olá! Meu nome é [SEU NOME] e esta é a apresentação do projeto **Cupcake Gourmet**, desenvolvido para a PIT II do curso de Engenharia de Software."

> "A situação-problema: uma loja de cupcakes gourmet teve uma experiência ruim com um sistema anterior mal planejado — processos de pedido confusos, dados perdidos, experiência ruim para o cliente e para o dono."

> "O objetivo da PIT I foi planejar. O da PIT II é **construir e documentar** um sistema funcional que resolva esses problemas."

---

### 🎬 Parte 2: Objetivo e Tecnologias (~30 segundos)

**Cena:** Mostrar o README ou um slide de apresentação.

> "Nosso objetivo foi criar uma aplicação **simples, funcional e organizada** para venda de cupcakes gourmet online, cobrindo do pedido ao acompanhamento."

> "As tecnologias escolhidas foram propositalmente enxutas:
> - **Frontend:** HTML5, CSS3 e JavaScript **puro** (sem React, sem frameworks)
> - **Backend:** Python com o microframework **Flask**
> - **Banco de Dados:** **SQLite** em arquivo (leve e sem servidor)
> - Comunicação via **Fetch API** com endpoints REST JSON."

> "Nada de exagero: só o necessário para um projeto acadêmico realista."

---

### 🎬 Parte 3: Página Inicial e Catálogo (~40 segundos)

**Cena:** Navegador aberto na página `index.html`. Navegar até produtos.

> "A página inicial apresenta a loja, um banner e os cupcakes em destaque. Vamos clicar em **Ver Produtos**."

> "Aqui temos o catálogo carregado **dinamicamente via API**: cada card mostra imagem, nome, descrição, categoria e preço. São seis produtos fictícios iniciais: Chocolate, Morango, Red Velvet, Baunilha, Nutella e Limão."

> "Vou adicionar **dois Cupcakes de Chocolate** e **um Red Velvet** ao carrinho."

---

### 🎬 Parte 4: Carrinho e Criação do Pedido (~60 segundos)

**Cena:** Página do `carrinho.html`, depois `finalizar.html`.

> "Abrindo o carrinho, vemos os itens adicionados. Consigo **aumentar/diminuir** quantidade e também **remover** itens. O subtotal e o total são recalculados automaticamente."

> "Agora vou **finalizar o pedido**: preencho nome, telefone, endereço, número, bairro, escolho a forma de pagamento — **Pix**, Dinheiro ou Cartão — e confirmo."

> "Aqui acontece o envio via **POST para a API Flask**, que salva tudo no banco SQLite: primeiro o pedido (tabela `orders`), depois cada item individual (tabela `order_items`)."

> "Pronto! Pedido finalizado com sucesso. Recebemos o **número #1** do pedido — esse número é a referência do cliente." *(anotar # na tela)*

---

### 🎬 Parte 5: Pedido Salvo no Banco e Acompanhamento (~45 segundos)

**Cena:** Mostrar banco (opcional), depois página `acompanhar.html`.

> "Vamos provar que foi salvo no banco: acessamos a página de acompanhamento e pesquisamos pelo número do pedido."

> "Traz todos os dados: cliente, total, pagamento, data/hora. E o principal: o **rastreador de status** com 4 etapas:
> 1. Pedido recebido
> 2. Em preparação
> 3. Saiu para entrega
> 4. Entregue"

> "No momento ele está na etapa 1, porque acabou de ser criado. Vamos para a área administrativa mudar isso."

---

### 🎬 Parte 6: Área Administrativa e Alteração de Status (~50 segundos)

**Cena:** Página `admin.html`. Mostrar abas Produtos e Pedidos.

> "A área administrativa tem duas abas. Primeiro: **Produtos** — consigo cadastrar, editar e excluir qualquer cupcake. Funcionalidade para manter o catálogo atualizado."

> "Agora a aba **Pedidos**: lista todos os pedidos com cliente, total, pagamento e status. Vou **ver os detalhes** do pedido #1 para confirmar tudo."

> "Confirmado. Agora vou **alterar o status** — primeiro para *Em preparação* (2), depois para *Saiu para entrega* (3), e depois para *Entregue* (4)."

> "Volto na página de acompanhamento e **atualizo a consulta** do mesmo pedido. Agora o status aparece como 'Entregue' com todas as etapas concluídas. Funciona em tempo real lendo do SQLite."

---

### 🎬 Parte 7: Testes, Correções e Qualidade (~25 segundos)

**Cena:** Mostrar arquivos na pasta docs/testes.md e laudo-qualidade.md + script de testes.

> "Para qualidade, fizemos **10 testes automatizados da API** cobrindo carregar produtos, CRUD, criar pedido, consultar e alterar status — todos passando."

> "Também preparamos a estrutura para **5 testes com colegas** e o laudo de qualidade — ambos com campos em branco para preenchermos após os testes reais com usuários."

> "Todo erro retorna mensagens amigáveis: 'Produto não encontrado', 'Carrinho vazio', 'Não foi possível carregar produtos' — nada de tela branca ou erro técnico."

---

### 🎬 Parte 8: Conclusão e Encerramento (~20 segundos)

**Cena:** Tela de agradecimento + volta à página inicial.

> "Concluindo: entregamos um sistema **simples, funcional, 100% acadêmico e coerente com a PIT I**. Frontend em HTML/CSS/JS puro, backend Flask, banco SQLite, documentação completa, testes e responsividade."

> "Funcionalidades futuras (que não implementamos agora): pagamento real, autenticação de usuários, notificações por WhatsApp/e-mail, integração com motoboy, testes mais completos e integração contínua."

> "Muito obrigado pela atenção! Fico à disposição para perguntas."

---

## 📋 Checklist de Gravação

- [ ] Microfone testado e com áudio limpo
- [ ] Tela gravada em 1080p ou superior
- [ ] Navegador em tela cheia durante demonstração
- [ ] Servidor Flask iniciado ANTES da gravação
- [ ] Dados de teste pré-preparados (não gravar enquanto digita devagar)
- [ ] Cortar momentos de silêncio ou erros
- [ ] Inserir legendas se possível
- [ ] Duração final: entre 4min30s e 5min30s
