"""Primeira etapa: um MCP server plano, rodando local sobre stdio.

Três ferramentas sobre um pequena database de "notas" SQLite. Sem network, sem autenticação.
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
    mcp.run() # stdio por padrão
