# mcp-notas

Estudo de MCP servers com FastMCP sobre SQLite. A etapa 1 roda local via stdio, sem rede; a etapa 2 expõe o mesmo servidor via Streamable HTTP, ainda sem autenticação.

## Estrutura

- `v1_local.py` — servidor MCP local (stdio) com três ferramentas:
  - `listar_minhas_notas()` — lista as notas.
  - `add_uma_nota(text)` — cria uma nota.
  - `deleta_uma_nota(note_id)` — apaga uma nota por id.
- `v2_remote.py` — o mesmo servidor, exposto em `http://localhost:8000/mcp` (sem autenticação).
- `notes_db.py` — camada SQLite: `add_note`, `delete_note`, `list_notes`.
- `notes.db` — banco criado automaticamente na primeira execução.
- `pyproject.toml` — dependências do projeto (`fastmcp`, `mcp`, `python-dotenv`).
- `.env.example` — variáveis para as próximas etapas (Descope).
- `pyrightconfig.json` — aponta o Pylance para o `.venv`.

## Rodando

```powershell
.\.venv\Scripts\Activate.ps1
pip install -e .
python v1_local.py
```

O servidor fala MCP via stdio, então ele é usado por um cliente MCP (não imprime nada no terminal).

Para a versão remota:

```powershell
python v2_remote.py
```

O servidor sobe em `http://localhost:8000/mcp` e fica disponível para qualquer cliente que alcance a URL. Nesta etapa não há autenticação: todos compartilham as notas do dono `"local"`.

## Usando no opencode

Troque `<caminho-do-projeto>` pelo caminho onde você clonou o repositório.

Para o servidor local (stdio):

```jsonc
{
  "mcp": {
    "notes-local": {
      "type": "local",
      "command": ["<caminho-do-projeto>/.venv/Scripts/python.exe", "<caminho-do-projeto>/v1_local.py"],
      "enabled": true
    }
  }
}
```

Para o servidor remoto, com o `v2_remote.py` rodando:

```jsonc
{
  "mcp": {
    "notes-remote": {
      "type": "remote",
      "url": "http://localhost:8000/mcp",
      "enabled": true
    }
  }
}
```
