import sys
from pathlib import Path
from unittest.mock import MagicMock

# Menambahkan folder utama proyek ke jalur pencarian Python
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR))

from Models.buku_model import BukuModel


def test_create_buku_berhasil():
    model = BukuModel()

    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    assert hasil is True
    mock_cursor.execute.assert_called_once()
    model.conn.commit.assert_called_once()


def test_get_all_buku_berhasil():
    model = BukuModel()

    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    data_buku = [
        {
            "id_buku": 1,
            "judul": "Buku Testing",
            "penulis": "Penulis QA",
            "tahun_terbit": 2026
        }
    ]

    mock_cursor.fetchall.return_value = data_buku

    hasil = model.get_all_buku()

    assert hasil == data_buku
    mock_cursor.execute.assert_called_once()
    mock_cursor.fetchall.assert_called_once()
    mock_cursor.close.assert_called_once()