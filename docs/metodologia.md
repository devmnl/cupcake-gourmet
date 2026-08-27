# Metodologia - Cupcake Gourmet

## 1. Como o Projeto Foi Desenvolvido

Este projeto foi desenvolvido individualmente por um estudante de Engenharia de Software, como parte da disciplina PIT II.

Para organizar o trabalho, eu utilizei o **Scrum de forma adaptada para projeto individual** — sem papéis fictícios como Product Owner ou Scrum Master, e sem equipe. A ideia foi só pegar emprestados alguns conceitos úteis do Scrum:

- **Backlog:** Uma lista com todas as tarefas que precisavam ser feitas, organizadas por prioridade.
- **Sprints:** Dividi o trabalho em 4 ciclos curtos de aproximadamente 1 semana cada.
- **Revisão:** No fim de cada Sprint, eu testava o que foi feito e ajustava o que precisava.

Essa abordagem serviu para não deixar tudo para a última semana e garantir que o projeto fosse avançando aos poucos.

---

## 2. Ferramentas e Tecnologias

| Categoria | Tecnologia | Uso no Projeto |
|-----------|------------|----------------|
| Front-end | HTML5 | Estrutura das páginas |
| Front-end | CSS3 | Estilos visuais e responsividade |
| Front-end | JavaScript (puro) | Interações, carrinho em `localStorage` e requisições `fetch()` |
| Back-end | Python 3 | Lógica do sistema e API |
| Back-end | Flask | Criação da API REST |
| Banco | SQLite 3 | Armazenar produtos, pedidos e itens (arquivo sem servidor) |
| Comunicação | Fetch API + JSON | Troca de dados entre o navegador e a API Flask |
| Testes | Script Python (`urllib.request`) | Testes básicos dos endpoints da API |
| Versionamento | Git + .gitignore | Controle de versão e preparação para GitHub |

*Não foram usados frameworks de front-end (React, Vue, Angular), TypeScript, Node.js, Bootstrap ou Tailwind — propositalmente, para manter o projeto simples e focado no básico da web.*

---

## 3. Ciclo de Vida: 4 Sprints

| Sprint | Duração Estimada | Foco |
|--------|------------------|------|
| **Sprint 1** | 1 semana | Estrutura do projeto, CSS, páginas inicial e de produtos |
| **Sprint 2** | 1 semana | Carrinho, finalização de pedido e criação da API + banco |
| **Sprint 3** | 1 semana | Acompanhamento de pedido e área administrativa |
| **Sprint 4** | 1 semana | Responsividade, correções, testes e documentação |

---

## 4. Processo Simples Para Cada Funcionalidade

Cada vez que eu implementava uma nova funcionalidade, seguia este roteiro básico:

1. **Ler o requisito / história de usuário** para entender exatamente o que precisava funcionar.
2. **Planejar o que mexer:** front-end só? back-end só? ou os dois?
3. **Implementar o back-end primeiro** (quando aplicável): endpoint Flask + SQL no banco.
4. **Depois implementar o front-end:** HTML (estrutura), CSS (visual) e JavaScript (interação / fetch).
5. **Testar manualmente no navegador:** testar o caminho feliz e também casos de erro (ex: carrinho vazio, campos em branco no formulário).
6. **Corrigir o que não funcionava direito.**
7. **Marcar a tarefa como concluída no backlog.**

---

## 5. Relação com a PIT I

Este projeto é a continuação direta da PIT I. Na PIT I eu fiz apenas o planejamento:
- Levantei requisitos funcionais e não funcionais
- Escrevi as histórias de usuário
- Criei o backlog com as 4 Sprints
- Desenhei wireframes simples e diagramas UML iniciais
- Planejei usar Scrum adaptado para desenvolvimento individual

Já na PIT II, o objetivo foi tirar esse planejamento do papel e construir o sistema de fato funcionando, além de documentar todas as etapas.
