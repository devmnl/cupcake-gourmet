# Deploy / Hospedagem - Cupcake Gourmet

Aqui estão algumas formas simples de colocar o sistema online para apresentação.  
Não é obrigatório hospedar — pode apresentar rodando localmente.

---

## Opção 1 — PythonAnywhere (gratuita, recomendada para projeto acadêmico)

O **PythonAnywhere** é a forma mais simples de hospedar Flask + SQLite gratuitamente.

Passos resumidos:

1. Criar conta gratuita em https://www.pythonanywhere.com
2. Subir os arquivos do projeto para lá (via Git ou upload)
3. Criar um ambiente virtual e instalar as dependências:
   ```
   mkvirtualenv cupcake
   pip install flask flask-cors
   ```
4. No painel, criar uma **Web App** → Configuração Manual → Python 3.10
5. Editar o arquivo WSGI para apontar para `app.py` do backend:
   ```python
   import sys
   sys.path.insert(0, '/home/SEU_USUARIO/cupcake-gourmet/backend')
   from app import app as application
   ```
6. Em Virtualenv path, colocar: `/home/SEU_USUARIO/.virtualenvs/cupcake`
7. (Opcional) Configurar arquivos estáticos em **Static Files** para servir o frontend
8. Clicar em **Reload** e acessar a URL

O arquivo `cupcake.db` será criado automaticamente no diretório do backend.

---

## Opção 2 — Rodar Localmente na Rede (para apresentação em sala)

Se a apresentação for na faculdade com rede local:

```
cd backend
pip install -r requirements.txt
python app.py
```

Se quiser que outros colegas acessem pelo IP da sua máquina, inicie o Flask com:
```
flask --app app run --host=0.0.0.0 --port=5000
```

Os colegas acessam no navegador:
```
http://SEU_IP:5000/static/index.html
```

*(Para isso funcionar, o Flask precisa servir os arquivos do frontend. Adicione as rotas `/` e `/static/<path>` no `app.py` se necessário.)*

---

## Opção 3 — Hospedar Backend no Render (passo a passo completo)

O Render é uma das plataformas mais fáceis para hospedar Flask gratuitamente (plano Free).

### Passo 0 — Preparar o repositório (já feito ✔️)

O seu repositório já está estruturado assim:
```
cupcake-gourmet/
├── backend/
│   └── app.py        ← Flask API
├── frontend/         ← HTML/CSS/JS
├── docs/
├── tests/
├── requirements.txt  ← Já inclui gunicorn
└── README.md
```

Seu `requirements.txt` deve ter 3 linhas:
```
Flask==3.0.0
flask-cors==4.0.0
gunicorn==21.2.0
```

### Passo 1 — Criar conta no Render

1. Acesse https://render.com
2. Clique em **Get Started** → faça login com sua conta do **GitHub** (assim ele conecta direto no repositório).
3. Autorize o Render a acessar o seu repo.

### Passo 2 — Criar um Web Service

1. No painel do Render, clique em **New** → **Web Service**
2. Selecione o seu repositório: `devmnl/cupcake-gourmet`
3. Clique em **Connect**

### Passo 3 — Configurar o serviço (TELA IMPORTANTE)

Preencha exatamente assim:

| Campo | Valor a colocar |
|-------|------------------|
| **Name** | `cupcake-gourmet-api` (ou qualquer nome, vai ficar na URL) |
| **Region** | `São Paulo` ou `Virginia` (qualquer um) |
| **Branch** | `main` |
| **Runtime** | **Python 3** |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `cd backend && gunicorn app:app` |
| **Plan** | **Free** (0 MB RAM / 0.5 CPU - de graça) |

### Passo 4 — Variáveis de Ambiente (opcional, não precisa)

Não precisa de nenhuma variável para o seu projeto. O SQLite já funciona direto.

### Passo 5 — Clicar em "Create Web Service"

Espere o build terminar. O Render vai:
1. Clonar seu repo do GitHub
2. Rodar `pip install -r requirements.txt` (instala Flask, flask-cors, gunicorn)
3. Rodar `cd backend && gunicorn app:app` (inicia a API)

Quando aparecer **"Live ⚡"** na barra superior, o backend está no ar!

A URL do backend vai ser algo tipo:
```
https://cupcake-gourmet-api.onrender.com
```

### Passo 6 — Testar a API online

No navegador, acesse:
```
https://SUA-URL.onrender.com/api/products
```

Deve aparecer a lista dos 6 cupcakes em JSON. Se aparecer, tá funcionando ✔️

### Passo 7 — Atualizar o frontend para apontar pro backend online

Abra CADA arquivo .js em `frontend/js/` e troque a linha:
```js
const API = 'http://localhost:5000/api';
```
ou
```js
const API_P = 'http://localhost:5000/api';
```

por:
```js
const API = 'https://SUA-URL.onrender.com/api';
```
ou
```js
const API_P = 'https://SUA-URL.onrender.com/api';
```

Arquivos que precisam ser editados:
- `produtos.js`
- `carrinho.js`
- `pedido.js`
- `acompanhar.js`
- `admin.js`

Depois commita e pusha:
```
git add .
git commit -m "Atualizada URL da API para Render"
git push
```

### Passo 8 — Hospedar o frontend no GitHub Pages (simples)

1. No GitHub, entre no repo → **Settings** → **Pages**
2. Em **Branch**, selecione `main` e a pasta **/ (root)** → Save
3. Depois de uns 2 minutos, o site fica online em:
   ```
   https://devmnl.github.io/cupcake-gourmet/frontend/
   ```
4. Testa o fluxo todo pelo site online!

### ⚠️ Aviso importante sobre SQLite no Render (Free)

Quando o Render fica sem acesso por uns 15 minutos, ele "dorme" a instância. Ao acordar, **o arquivo `cupcake.db` pode ser apagado** (porque o Render recria a pasta temporária).

Isso significa que:
- Os **6 produtos iniciais** são recriados automaticamente (tem seed no `app.py`) ✔️
- **Pedidos feitos antes do "sono"** podem sumir 😕

Para trabalho acadêmico isso costuma ser aceitável (basta avisar ao professor sobre essa limitação da hospedagem gratuita). Se quiser preservar os dados permanentemente, precisa usar um banco externo tipo PostgreSQL ou migrar pro PythonAnywhere (Opção 1).

---

## Pendências para preencher depois

| Item | Valor |
|------|-------|
| Plataforma escolhida: | |
| URL do backend (API): | |
| URL do frontend (site): | |
| Data do deploy: | |
| Observações: | |
