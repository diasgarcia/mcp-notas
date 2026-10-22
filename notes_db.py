import sqlite3
from contextlib import closing
from pathlib import Path

DB_PATH = Path(__file__).with_name("notes.db")


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner TEXT NOT NULL,
            text TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        )
        """
    )
    return conn


def list_notes(owner: str) -> list[dict]:
    """Lista as notas de um dono, da mais antiga para a mais nova."""
    with closing(_connect()) as conn, conn:
        rows = conn.execute(
            "SELECT id, owner, text, created_at FROM notes WHERE owner = ? ORDER BY id",
            (owner,),
        ).fetchall()
    return [dict(row) for row in rows]


def add_note(owner: str, text: str) -> dict:
    """Insere uma nota e devolve a linha criada."""
    with closing(_connect()) as conn, conn:
        cursor = conn.execute(
            "INSERT INTO notes (owner, text) VALUES (?, ?)", (owner, text)
        )
        row = conn.execute(
            "SELECT id, owner, text, created_at FROM notes WHERE id = ?",
            (cursor.lastrowid,),
        ).fetchone()
    return dict(row)


def delete_note(owner: str, note_id: int) -> bool:
    """Remove uma nota do dono; False se não existir."""
    with closing(_connect()) as conn, conn:
        cursor = conn.execute(
            "DELETE FROM notes WHERE id = ? AND owner = ?", (note_id, owner)
        )
    return cursor.rowcount > 0
