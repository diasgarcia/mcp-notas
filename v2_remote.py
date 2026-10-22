"""Segunda etapa: o mesmo servidor, mas remoto (Streamable HTTP) SEM autenticação

Run: python v2_remote.py
URL: http://localhost:8000/mcp

Qualquer um que alcançe essa url pode listar, adicionar e deletar notas. Não temos ideia
de "quem" está chamando, assim todos que chamam veem as mesmas notas. O V3 vai resolver
esse problema.
"""

from fastmcp import FastMCP

from notes_db import add_note, delete_note, list_notes

mcp = FastMCP("notes")


@mcp.tool()
def listar_minhas_notas() -> list[dict]:
    """Lista todas as minhas notas salvas."""
    return list_notes(owner="local")

@mcp.tool()
def add_uma_nota(text: str) -> dict:
    """Salva uma nova nota."""
    return add_note(owner="local", text=text)

@mcp.tool()
def deleta_uma_nota(note_id: int) -> str:
    """Deleta uma nota por id."""
    return "deleted" if delete_note(owner="local", note_id=note_id) else "não achado"

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
