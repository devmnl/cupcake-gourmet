# Deploy e Hospedagem - Cupcake Gourmet

> Documentação de como hospedar o projeto Flask + SQLite de forma simples.
> NÃO é necessário configurar infraestrutura complexa.
> **Links e configurações reais serão inseridos posteriormente pelo estudante.**

---

## 1. Visão Geral da Arquitetura para Deploy

O sistema tem duas partes que precisam ser hospedadas:

| Parte | Tecnologia | O que faz |
|-------|------------|-----------|
| **Frontend** | HTML + CSS + JS (estáticos) | Páginas que o usuário abre no navegador |
| **Backend** | Python + Flask + SQLite | API REST que lê/grava dados |

Como o SQLite é um banco em arquivo, o Flask serve tanto a API quanto pode servir também os arquivos estáticos (opção mais simples).

---

## 2. Opção Mais Simples: PythonAnywhere (Recomendado para Acadêmico)

**PythonAnywhere** é uma plataforma gratuita (plano beginner) para hospedar aplicações Python. É a opção mais simples para este projeto.

### Passos Resumidos:

1. **Criar conta** em https://www.pythonanywhere.com (gratuita)
2. **Fazer upload** do projeto (via Files, Git ou GitHub)
3. **Configurar o ambiente virtual:**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 cupcakeenv
   pip install -r /home/SEU_USUARIO/cupcake-gourmet/requirements.txt
   ```
4. **Adicionar uma nova Web App** no painel → **Manual Configuration** → Python 3.10
5. **Editar o arquivo WSGI** (`/var/www/SEU_USUARIO_pythonanywhere_com_wsgi.py`) com algo como:
   ```python
   import sys
   path = '/home/SEU_USUARIO/cupcake-gourmet/backend'
   if path not in sys.path:
       sys.path.insert(0, path)
   from app import app as application
   ```
6. **Configurar Virtualenv path** no painel da Web App:
   `/home/SEU_USUARIO/.virtualenvs/cupcakeenv`
7. **Configurar Static Files** (para servir o frontend):
   - URL: `/static/`
   - Directory: `/home/SEU_USUARIO/cupcake-gourmet/frontend/`
8. **Reload da aplicação**
9. Acessar: `https://SEU_USUARIO.pythonanywhere.com/static/index.html`

O arquivo `cupcake.db` (SQLite) será criado automaticamente no diretório do backend.

---

## 3. Opção Alternativa: Hospedar Frontend e Backend Separados

### 3.1 Backend: Render / Railway / Fly.io

Plataformas PaaS que suportam Python. Processo semelhante:

1. Subir o projeto para GitHub
2. Conectar a plataforma ao repositório
3. Configurar Build Command:
   ```bash
   pip install -r requirements.txt
   ```
4. Configurar Start Command:
   ```bash
   cd backend && gunicorn app:app
   ```
   *(Instalar `gunicorn` adicionando-o ao requirements.txt)*
5. Configurar **porta** como variável de ambiente (a plataforma define).

⚠️ **Atenção com SQLite em PaaS:** Muitas plataformas (como Render free tier) reiniciam o disco periodicamente, apagando o arquivo `.db`. Para projeto acadêmico temporário isso geralmente é aceitável. Para permanente, migrar para PostgreSQL.

### 3.2 Frontend: GitHub Pages / Netlify / Vercel (Estáticos)

1. Subir a pasta `frontend/` para GitHub Pages ou arrastar para Netlify
2. **Alterar a URL da API** em todos os arquivos `.js` e inline `<script>`:
   - De: `http://localhost:5000/api`
   - Para: `https://SEU_BACKEND.onrender.com/api` (exemplo)

---

## 4. Opção Local + Acesso na Rede (Para Apresentação)

Se a apresentação for presencial com uma rede local:

```bash
# No backend
pip install -r requirements.txt
cd backend
flask --app app run --host=0.0.0.0 --port=5000
```

Os colegas acessam pelo IP da sua máquina:
```
http://SEU_IP_LOCAL:5000/static/index.html
```

⚠️ Requer que o Flask sirva também os arquivos estáticos (adicionar em `app.py`):
```python
from flask import send_from_directory
import os

@app.route('/')
def index():
    return send_from_directory(os.path.join('..', 'frontend'), 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(os.path.join('..', 'frontend'), path)
```

---

## 5. Checklist Pré-Deploy

- [ ] Remover `debug=True` do `app.run()` em produção
- [ ] Alterar CORS para aceitar apenas a URL do frontend público:
  ```python
  CORS(app, resources={r"/api/*": {"origins": "https://SEU_SITE.com"}})
  ```
- [ ] Confirmar que `cupcake.db` tem permissões de leitura e escrita (chmod 666)
- [ ] Testar fluxo completo: adicionar produto → carrinho → pedido → consultar
- [ ] Atualizar a variável `API_URL` nos arquivos JS para o domínio público

---

## 6. Informações Pendentes (Preencher Depois)

| Campo | Valor |
|-------|-------|
| **Plataforma escolhida:** | ________________________________________ |
| **URL do Backend (API):** | ________________________________________ |
| **URL do Frontend (Site):** | ________________________________________ |
| **Data do deploy:** | ____/____/________ |
| **Observações:** | <br><br> |
