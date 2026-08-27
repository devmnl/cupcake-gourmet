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

## Opção 3 — Hospedar Front e Back Separados

### Backend: Render / Railway
São plataformas PaaS que rodam Python. Basta conectar o repositório do GitHub e configurar:
- Build: `pip install -r requirements.txt`
- Run: `cd backend && gunicorn app:app` (adicione `gunicorn` no requirements.txt)

⚠️ Atenção: o SQLite nessas plataformas (plano gratuito) geralmente é apagado quando o servidor reinicia. Para trabalho acadêmico temporário costuma ser ok.

### Frontend: GitHub Pages / Netlify
Suba a pasta `frontend` como site estático e depois altere a URL da API nos arquivos `.js` para o endereço do backend.

---

## Pendências para preencher depois

| Item | Valor |
|------|-------|
| Plataforma escolhida: | |
| URL do backend (API): | |
| URL do frontend (site): | |
| Data do deploy: | |
| Observações: | |
