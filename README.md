# mcp-notas

Estudo de MCP servers locais com FastMCP sobre SQLite. Sem rede e sem autenticação (etapa 1).

## Estrutura

- `v1_local.py` — servidor MCP local (stdio) com três ferramentas:
  - `listar_minhas_notas()` — lista as notas.
  - `add_uma_nota(text)` — cria uma nota.
  - `deleta_uma_nota(note_id)` — apaga uma nota por id.
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

## Usando no opencode

Troque `<caminho-do-projeto>` pelo caminho onde você clonou o repositório.

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
