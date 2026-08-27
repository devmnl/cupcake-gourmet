# Metodologia - Cupcake Gourmet

## 1. Metodologia de Desenvolvimento

### Scrum (Adaptado para Projeto Individual Acadêmico)

O desenvolvimento do sistema **Cupcake Gourmet** seguiu a metodologia ágil **Scrum**, adaptada para um projeto individual conforme utilizado na PIT I. A escolha do Scrum se justifica pela necessidade de entregas incrementais, organização do backlog e ciclos curtos de desenvolvimento (Sprints), alinhados ao cronograma acadêmico.

### Pilares do Scrum Aplicados
- **Transparência:** Todo o progresso é registrado no backlog do produto, com status e sprint de cada tarefa.
- **Inspeção:** Revisão ao final de cada sprint para validar o incremento e identificar ajustes.
- **Adaptação:** Ajustes no backlog e na estratégia conforme dificuldades encontradas.

---

## 2. Papéis (Projeto Individual)

Em um projeto individual, os três papéis do Scrum são acumulados:

| Papel | Responsabilidade no Projeto |
|-------|------------------------------|
| **Product Owner (PO)** | Define as funcionalidades conforme os requisitos da PIT II, prioriza o backlog de acordo com importância acadêmica e valor para o cliente fictício. |
| **Scrum Master (SM)** | Auto-organização do cronograma, identificação e remoção de impedimentos (ex: dificuldade com CORS, dúvidas em SQL), garantia do cumprimento das Sprints. |
| **Development Team (Dev)** | Implementação técnica completa: modelagem do banco, API Flask, frontend HTML/CSS/JS, testes e documentação. |

---

## 3. Ciclo de Vida: 4 Sprints

O projeto foi organizado em **4 Sprints** de aproximadamente 1 semana cada, alinhados com o ciclo de entrega da disciplina:

| Sprint | Período Estimado | Objetivo Principal | Entregas Chave |
|--------|------------------|--------------------|----------------|
| **Sprint 1** | Semana 1 | Interface e Catálogo | Estrutura de pastas, CSS identidade visual, página inicial, página de produtos com consumo da API (GET). |
| **Sprint 2** | Semana 2 | Carrinho e Pedidos | Carrinho com localStorage, página de finalização, Flask API de pedidos (POST), SQLite salvando orders e order_items. |
| **Sprint 3** | Semana 3 | Banco e Administração | CRUD completo de produtos, página de acompanhamento com tracker de status, área administrativa (listar pedidos, detalhes, alterar status). |
| **Sprint 4** | Semana 4 | Testes, Correções e Documentação | Responsividade mobile/tablet, tratamento de erros, testes automatizados, toda documentação acadêmica em `docs/`, README, `.gitignore`, `requirements.txt`. |

### Eventos Scrum (Equivalente Individual)

| Evento Scrum | Como foi adaptado |
|--------------|-------------------|
| **Sprint Planning** | No início de cada Sprint: selecionar os itens do backlog, definir meta da Sprint. |
| **Daily Scrum** | Check diário auto-aplicado: O que fiz ontem? O que farei hoje? Quais impedimentos? (registrado em anotações pessoais) |
| **Sprint Review** | Ao final de cada Sprint: testar o incremento, validar funcionalidades, registrar o que está pronto vs. o que precisa de ajuste. |
| **Sprint Retrospective** | Lições aprendidas por Sprint: o que deu certo? o que pode melhorar na próxima? (ex: na Sprint 1 aprendi a organizar melhor os endpoints antes de codar). |

---

## 4. Ferramentas Utilizadas

| Categoria | Ferramenta | Finalidade |
|-----------|------------|------------|
| **Linguagem Front** | HTML5, CSS3, JavaScript (puro - ES6+) | Interface, estilos e interações do usuário. |
| **Linguagem Back** | Python 3 | Lógica de negócio e API. |
| **Framework Web** | Flask | API REST leve para endpoints. |
| **Banco de Dados** | SQLite 3 | Persistência relacional (em arquivo). |
| **CORS** | Flask-CORS | Permitir requisições do frontend separado. |
| **Armazenamento Local** | localStorage API (Browser) | Carrinho temporário do cliente. |
| **IDE / Editor** | Editor de código-fonte com suporte a HTML/CSS/JS/Python | Codificação. |
| **Navegador** | Navegador moderno (Chrome/Edge/Firefox) | Testes de interface. |
| **Versionamento** | Git + .gitignore | Controle de versões (preparado para GitHub). |
| **Testes** | Script Python com urllib.request | Testes automatizados dos endpoints. |
| **Comunicação** | Fetch API (JS) | Comunicação assíncrona JS ↔ Flask. |

---

## 5. Processo de Desenvolvimento por Funcionalidade

Cada funcionalidade seguiu este ciclo simplificado:

```
1. ANÁLISE
   └─ Ler requisito / história de usuário
   └─ Identificar o que precisa ser feito (frontend / backend / ambos)

2. PROJETO SIMPLES
   └─ Definir estrutura da tela OU estrutura do endpoint
   └─ Definir campos e validações

3. IMPLEMENTAÇÃO
   └─ Codificar backend (API + SQL)
   └─ Codificar frontend (HTML + CSS + JS fetch)

4. VALIDAÇÃO
   └─ Testar manualmente no navegador
   └─ Testar caso de erro (ex: carrinho vazio, produto inexistente)
   └─ Registrar correções se houver

5. INTEGRAÇÃO
   └─ Garantir que funcionalidade nova não quebrou funcionalidades anteriores
```

---

## 6. Critérios de Pronto (Definition of Done)

Uma tarefa só é considerada **Concluída** quando:

- [x] Código implementado e sintaticamente correto;
- [x] Funciona no navegador desktop e responsivo (celular);
- [x] Comunicação com API funcionando (quando aplicável);
- [x] Dados sendo salvos/lidos corretamente no SQLite;
- [x] Mensagens de erro amigáveis para casos de falha;
- [x] Validado contra a história de usuário e critérios de aceitação;
- [x] Registrado no backlog como ✅ Concluído.

---

## 7. Alinhamento com a PIT I

Esta metodologia dá **continuidade direta** à PIT I:
- Mantém Scrum como framework.
- Mantém histórias de usuário e backlog como artefatos centrais.
- Evolui da fase de *planejamento e prototipação* (PIT I) para *implementação, validação e documentação* (PIT II).
- Requisitos funcionais e não funcionais da PIT I foram a base direta do Product Backlog.
