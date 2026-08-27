# Roteiro do Vídeo de Apresentação - Cupcake Gourmet

Vídeo estimado em ~5 minutos. Fale naturalmente, como se estivesse explicando para um colega ou professor.

---

## Parte 1 — Introdução (~30 segundos)

Tela inicial do site aberta.

> "Olá! Meu nome é [SEU NOME] e esta é a apresentação do **Cupcake Gourmet**, o projeto que desenvolvi para a PIT II do curso de Engenharia de Software."

> "Na PIT I eu planejei todo o sistema — requisitos, histórias de usuário, backlog, diagramas. Agora na PIT II eu implementei tudo funcionando."

---

## Parte 2 — Tecnologias (~30 segundos)

Mostre o README ou a estrutura de pastas.

> "Para o desenvolvimento eu utilizei tecnologias simples que aprendi na faculdade:
> - No front-end: **HTML5, CSS3 e JavaScript puro** — sem nenhum framework como React ou Vue."
> - No back-end: **Python com Flask** para criar a API."
> - No banco: **SQLite** — um banco em arquivo, sem precisar instalar servidor."

> "A comunicação entre eles é feita com **fetch API** e JSON."

---

## Parte 3 — Cliente: Visualizando Produtos e Montando o Carrinho (~1 minuto)

Abra `index.html` no navegador, navegue até produtos.

> "Essa é a página inicial, com um destaque de produtos. Vou clicar em **Produtos** para ver o catálogo completo."

> "Aqui são carregados 6 cupcakes fictícios via API. Cada um tem imagem, nome, descrição, categoria e preço. Vou adicionar **2 cupcakes de chocolate** e **1 Red Velvet** ao carrinho."

---

## Parte 4 — Carrinho e Finalização do Pedido (~1 minuto)

Vá para o carrinho, depois finalize.

> "Abrindo o carrinho, aparecem os itens que adicionei. Consigo mudar a quantidade com os botões + e -, e também remover itens. O total é calculado automaticamente."

> "Agora vou clicar em **Finalizar Pedido**. Preencho nome, telefone, endereço, número, bairro, escolho a forma de pagamento — neste caso **Dinheiro** — e confirmo."

> "Pronto! O pedido foi salvo no banco com sucesso e me retornou o **número 1**. Vou anotar esse número para consultar depois."

---

## Parte 5 — Consultando o Status do Pedido (~30 segundos)

Abra `acompanhar.html`.

> "Agora vou para a tela de **Acompanhar** para pesquisar pelo número do pedido que acabei de criar."

> "Ele me mostra os dados do pedido: cliente, total, pagamento, data e o status visual com 4 etapas. No momento ele está como **Pedido recebido**. Vou para a área admin para mudar o status."

---

## Parte 6 — Área Administrativa (~1 minuto)

Abra `admin.html`.

> "A área administrativa tem duas abas: **Produtos** e **Pedidos**."

> "Na aba Produtos, eu consigo **cadastrar, editar e excluir** qualquer cupcake. Serve para manter o catálogo atualizado."

> "Na aba Pedidos, aparecem todos os pedidos. Vou clicar em **Status** no pedido #1 e alterar para **Em preparação (2)**, depois para **Saiu para entrega (3)** e por fim **Entregue (4)**."

> "Agora se eu voltar na tela de acompanhamento e pesquisar novamente, o status aparece como concluído."

---

## Parte 7 — Testes e Conclusão (~30 segundos)

Mostre a pasta `docs/` e o arquivo de testes.

> "Para qualidade, eu implementei **4 testes automatizados básicos** da API: listar produtos, criar pedido, consultar pedido e alterar status. Todos passando."

> "Também preparei a estrutura para **5 testes com colegas** e o laudo de qualidade — ambos serão preenchidos após os testes reais."

> "Concluindo: o sistema está funcionando como foi planejado na PIT I, utilizando tecnologias simples e adequadas para um projeto acadêmico. Obrigado pela atenção!"

---

## Checklist antes de gravar

- [ ] Microfone funcionando
- [ ] Backend Flask já iniciado ANTES de gravar
- [ ] Dados de teste já preparados (não precisa gravar enquanto digita devagar)
- [ ] Navegador em tela cheia
- [ ] Duração entre 4min30s e 5min30s
- [ ] Se possível, adicionar legendas
