# Backlog do Produto - Cupcake Gourmet

## Product Backlog

Lista das tarefas planejadas e o status de cada uma:

| ID | Tarefa | Prioridade | Sprint | Status |
|----|--------|------------|--------|--------|
| PB-01 | Criar estrutura de pastas do projeto | Alta | 1 | Concluído |
| PB-02 | Criar CSS com identidade visual de cupcakes | Alta | 1 | Concluído |
| PB-03 | Criar página inicial (index.html) | Alta | 1 | Concluído |
| PB-04 | Criar página de produtos (produtos.html) | Alta | 1 | Concluído |
| PB-05 | Configurar Flask e criar API de produtos | Alta | 2 | Concluído |
| PB-06 | Criar tabelas SQLite (products, orders, order_items) | Alta | 2 | Concluído |
| PB-07 | Inserir 6 produtos iniciais no banco | Alta | 2 | Concluído |
| PB-08 | Implementar JS para carregar produtos via API | Alta | 1 | Concluído |
| PB-09 | Criar página do carrinho (carrinho.html) | Alta | 2 | Concluído |
| PB-10 | Implementar carrinho no localStorage (add/remove/qtd) | Alta | 2 | Concluído |
| PB-11 | Calcular subtotal e total em tempo real | Alta | 2 | Concluído |
| PB-12 | Criar página de finalização (finalizar.html) | Alta | 2 | Concluído |
| PB-13 | Implementar validações do formulário de pedido | Alta | 2 | Concluído |
| PB-14 | Criar endpoint POST /api/orders para salvar pedido | Alta | 2 | Concluído |
| PB-15 | Criar página de acompanhamento (acompanhar.html) | Média | 3 | Concluído |
| PB-16 | Implementar consulta por número do pedido | Média | 3 | Concluído |
| PB-17 | Implementar visualizador de status (stepper) | Média | 3 | Concluído |
| PB-18 | Criar área administrativa (admin.html) | Média | 3 | Concluído |
| PB-19 | CRUD de produtos na área admin | Média | 3 | Concluído |
| PB-20 | Listar e ver detalhes de pedidos na admin | Média | 3 | Concluído |
| PB-21 | Alterar status do pedido na admin | Média | 3 | Concluído |
| PB-22 | Ajustar responsividade para celular/tablet | Alta | 4 | Concluído |
| PB-23 | Melhorar mensagens de erro para o usuário | Alta | 4 | Concluído |
| PB-24 | Criar testes automatizados básicos da API | Média | 4 | Concluído |
| PB-25 | Escrever documentação (requisitos, histórias, backlog...) | Média | 4 | Concluído |
| PB-26 | Desenhar diagramas UML (casos de uso e classes) | Média | 4 | Concluído |
| PB-27 | Criar wireframes das telas principais | Média | 4 | Concluído |
| PB-28 | Preparar estrutura para 5 testes com colegas | Média | 4 | Concluído |
| PB-29 | Preparar laudo de qualidade (template vazio) | Média | 4 | Concluído |
| PB-30 | Criar pasta de evidências | Média | 4 | Concluído |
| PB-31 | Documentar sugestões de deploy/hospedagem | Baixa | 4 | Concluído |
| PB-32 | Preparar roteiro do vídeo de apresentação | Baixa | 4 | Concluído |
| PB-33 | Escrever README do repositório | Alta | 4 | Concluído |
| PB-34 | Criar requirements.txt e .gitignore | Alta | 4 | Concluído |
| PB-35 | Testar manualmente e corrigir bugs | Alta | 4 | Concluído |

---

## Sprints

O projeto foi organizado em 4 ciclos curtos (Sprints) de aproximadamente 1 semana cada, para organizar o desenvolvimento individual:

### Sprint 1 — Interface e Catálogo
- Objetivo: montar a estrutura do front-end e fazer os produtos aparecerem
- Entregas: estrutura de pastas, CSS, página inicial, página de produtos e JavaScript para carregar produtos da API

### Sprint 2 — Carrinho e Pedidos
- Objetivo: permitir que o cliente monte o carrinho e finalize a compra
- Entregas: carrinho no localStorage, página de carrinho, página de finalização, Flask API de pedidos e tabelas do SQLite

### Sprint 3 — Acompanhamento e Administração
- Objetivo: permitir consulta de status e gerenciamento da loja
- Entregas: página de acompanhamento com stepper, área administrativa com CRUD de produtos e gestão de pedidos/status

### Sprint 4 — Testes, Correções e Documentação
- Objetivo: finalizar detalhes e entregar tudo documentado
- Entregas: responsividade, tratamento de erros, testes básicos, documentação em `docs/`, README, requirements e .gitignore

---

## Sobre a Organização (Scrum Adaptado)

Como o projeto foi feito por apenas uma pessoa (estudante), o Scrum foi usado de forma simplificada:
- Não há Product Owner, Scrum Master ou equipe fictícios — sou eu mesmo organizando as tarefas.
- O backlog acima serviu como lista do que precisa ser feito, com prioridade.
- As Sprints foram ciclos de 1 semana para entregar partes funcionantes do sistema.
- No final de cada Sprint, eu revisava o que funcionou e o que precisava ser ajustado antes da próxima etapa.

Essa adaptação foi suficiente para organizar o trabalho sem complicações.
