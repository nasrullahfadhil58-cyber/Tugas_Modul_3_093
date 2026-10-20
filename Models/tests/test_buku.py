import sys
from pathlib import Path
from unittest.mock import MagicMock

# Menambahkan folder utama proyek ke jalur pencarian Python
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR))

from Models.buku_model import BukuModel


def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi koneksi database agar tidak memakai database asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi hasil
    assert hasil is True
    mock_cursor.execute.assert_called_once()
    model.conn.commit.assert_called_once()
