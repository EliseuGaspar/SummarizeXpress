# Summarizexpress

## Descrição

### O que é?

Summarizexpress é uma plataforma online para criação autómatica de resumo de conteúdos. Resumos estes que podem ser à base de ficheiros, imagens e até mesmo urls.

### Como funciona?

Atravéz de ficheiros como documentos e imagens, e até mesmo links para landing pages o **summarizexpress** gera um resumo recheado e detalhado do conteúdo para o usuário, minizando assim o tempo e trazendo o excencial do grande volume de informação!

### Arquitetura

O **summarizexpress** é projetado a base da arquitetura MVC. Para mais informações sobre consulte a pasta [Docs](./docs/index.md).

### Tecnologias

Para a construção desta plataforma as seguintes tecnologias foram usadas:

 - Linguagens de Programação:
   - Python
   - Typescript
 - Frameworks:
   - FastAPI
   - NextJS
 - Banco de Dados:
   - Sqlite3
 - Editor de Código:
   - VSCode

Para mais informações consulte a pasta [Docs](./docs/index.md).

### Como rodar?

Para rodar o projeto basta seguir os seguintes passos:

**1º** - Fazer o gitclone do projeto

```bash
git clone https://github.com/eliseugaspar/
```

**2º** - Criar um ambiente virtual

```bash
python -m venv venv
```

**3º** - Instalar todas as dependencias do projeto

```bash
pip install -r requirements.txt
```

**4º** - Rodar o projeto

```bash
uvicorn --port 8000 --host 0.0.0.0 server:api
```

