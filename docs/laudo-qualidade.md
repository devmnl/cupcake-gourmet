# Laudo de Qualidade - Cupcake Gourmet



---

## Resumo

| Campo | Informação |
|-------|------------|
| Versão do sistema testada: | 1.0 (PIT II) |
| Data do laudo: | 27/08/2026 *(simulada)* |
| Responsável: | Manu *(substituir pelo nome completo na versão final)* |
| Ambiente de teste: | Python + Flask + SQLite + navegador web |
| Total de problemas encontrados: | 4 |
| Total de problemas corrigidos: | 4 |
| Total pendentes: | 0 |

---

## Registro de Problemas

### Problema #1

| Campo | Conteúdo |
|-------|----------|
| **Problema:** | Dificuldade para remover um produto do carrinho |
| **Tela / Funcionalidade:** | Carrinho |
| **Descrição:** | Durante o teste, foi percebido que não ficou muito claro como remover um produto quando sua quantidade era diminuída. |
| **Evidência (print/nome do arquivo):** | `evidencias/problema-carrinho.png`  |
| **Correção realizada:** | Foi melhorada a indicação do botão de remover o produto. |
| **Resultado após correção:** | A opção de remover ficou mais fácil de identificar. |
| **Status:** | ✅ Corrigido |

---

### Problema #2

| Campo | Conteúdo |
|-------|----------|
| **Problema:** | Campo de busca pouco explicativo |
| **Tela / Funcionalidade:** | Página de produtos |
| **Descrição:** | Um dos testes mostrou que não ficou muito claro que a busca deveria ser feita pelo nome do produto. |
| **Evidência (print/nome do arquivo):** | `evidencias/busca-produto.png`  |
| **Correção realizada:** | O texto do campo de busca foi alterado para deixar sua função mais clara. |
| **Resultado após correção:** | A finalidade do campo ficou mais fácil de entender. |
| **Status:** | ✅ Corrigido |

---

### Problema #3

| Campo | Conteúdo |
|-------|----------|
| **Problema:** | Mensagem pouco clara no preenchimento do pedido |
| **Tela / Funcionalidade:** | Finalização do pedido |
| **Descrição:** | Quando um campo obrigatório não era preenchido, a mensagem não explicava claramente o que precisava ser corrigido. |
| **Evidência (print/nome do arquivo):** | `evidencias/validacao-pedido.png`  |
| **Correção realizada:** | As mensagens dos campos obrigatórios foram melhoradas. |
| **Resultado após correção:** | Ficou mais fácil identificar o campo que precisava ser preenchido. |
| **Status:** | ✅ Corrigido |

---

### Problema #4

| Campo | Conteúdo |
|-------|----------|
| **Problema:** | Pouco espaço entre alguns elementos em telas menores |
| **Tela / Funcionalidade:** | Área administrativa |
| **Descrição:** | Durante o teste em uma tela menor, alguns elementos da área administrativa ficaram muito próximos. |
| **Evidência (print/nome do arquivo):** | `evidencias/admin-mobile.png`  |
| **Correção realizada:** | Foram ajustados os espaços entre alguns elementos da tela administrativa. |
| **Resultado após correção:** | A tela ficou mais organizada em tamanhos menores. |
| **Status:** | ✅ Corrigido |

---

## Resultado dos Testes Automatizados Básicos

| Teste | Descrição | Resultado | Observações |
|-------|-----------|-----------|-------------|
| T1 | Listar produtos (GET /api/products) | ✅ | Os produtos foram retornados normalmente. |
| T2 | Criar pedido (POST /api/orders) | ✅ | O pedido foi criado corretamente. |
| T3 | Consultar pedido (GET /api/orders/:id) | ✅ | O pedido foi encontrado pelo número informado. |
| T4 | Alterar status (PUT /api/orders/:id/status) | ✅ | O status do pedido foi alterado corretamente. |

---

## Conclusão

| Pergunta | Resposta |
|----------|----------|
| O sistema atende aos requisitos funcionais? | ☑ Sim / ⬜ Parcialmente / ⬜ Não |
| O sistema está responsivo? | ☑ Sim / ⬜ Parcialmente / ⬜ Não |
| Está estável para apresentação? | ☑ Sim / ⬜ Sim com ressalvas / ⬜ Não |

### Comentários finais

Os testes simulados mostraram que as principais funções do sistema estão funcionando corretamente.

Foram identificadas algumas pequenas dificuldades durante o uso, principalmente relacionadas à clareza de alguns botões, mensagens e ao espaço disponível em telas menores.

As correções realizadas deixaram o sistema mais fácil de utilizar e mais organizado.

De forma geral, o Cupcake Gourmet apresenta as principais funções propostas para o projeto, como visualização dos produtos, carrinho, realização de pedidos, acompanhamento e administração dos produtos e pedidos.

