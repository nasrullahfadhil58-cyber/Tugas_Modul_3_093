
# Sistem Manajemen Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Manajemen Perpustakaan merupakan aplikasi desktop berbasis Python yang digunakan untuk mengelola data buku. Aplikasi ini menggunakan CustomTkinter sebagai antarmuka pengguna dan MySQL sebagai basis data. Sistem menerapkan pola arsitektur Model-View-Controller (MVC) serta autentikasi pengguna berdasarkan peran admin dan anggota. Admin dapat menambah, memperbarui, dan menghapus data buku, sedangkan anggota dapat melihat data buku.

## 2. Struktur Direktori MVC

Struktur direktori utama proyek adalah sebagai berikut:

```text
Tugas_Modul3/
├── config/
│   └── database.py
├── controllers/
│   ├── auth_controller.py
│   ├── buku_controller.py
│   └── anggota_controller.py
├── models/
│   ├── buku_model.py
│   ├── user_model.py
│   └── tests/
│       ├── test_auth.py
│       └── test_buku.py
├── views/
│   ├── login_view.py
│   ├── buku_view.py
│   └── anggota_view.py
├── templates/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
├── main.py
├── requirements.txt
└── README.md
```

Keterangan:

- **Model** mengelola data dan komunikasi dengan database MySQL.
- **View** menampilkan antarmuka aplikasi kepada pengguna.
- **Controller** mengatur alur aplikasi dan menghubungkan Model dengan View.
- **Config** menyimpan konfigurasi koneksi database.
- **Tests** berisi pengujian otomatis untuk memeriksa fungsi aplikasi.

## 3. Panduan Instalasi dan Konfigurasi Database MySQL

### A. Persiapan

Pastikan perangkat telah memiliki:
- Python 3.11 atau versi yang kompatibel dengan proyek.
- Laragon atau server MySQL/MariaDB.
- Visual Studio Code.
- Git (opsional, untuk mengambil proyek dari GitHub).

### B. Membuka Proyek

Buka terminal pada direktori proyek:

```powershell
cd C:\tugas_Modul3
```

### C. Membuat Virtual Environment

Buat lingkungan Python terpisah:

```powershell
python -m venv .venv
```

Aktifkan virtual environment di Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Jika PowerShell menolak aktivasi, jalankan perintah berikut terlebih dahulu:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Kemudian aktifkan kembali virtual environment.

### D. Menginstal Dependensi

Pastikan virtual environment aktif, lalu jalankan:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### E. Konfigurasi Database

1. Buka Laragon dan jalankan layanan MySQL.
2. Buka phpMyAdmin atau MySQL client.
3. Buat database dengan nama `db_perpustakaan_rpl` jika database tersebut belum tersedia.
4. Pastikan tabel yang diperlukan aplikasi, seperti `users` dan `buku`, telah dibuat sesuai struktur yang digunakan pada proyek.
5. Periksa file `config/database.py` dan sesuaikan host, port, username, password, serta nama database dengan konfigurasi MySQL lokal.

Contoh konfigurasi koneksi yang perlu disesuaikan:

```text
Host     : localhost
Port     : 3306
Database : db_perpustakaan_rpl
Username : root
Password : Sesuaikan dengan konfigurasi MySQL
```

Pastikan struktur tabel dan akun pengguna telah tersedia sebelum menjalankan aplikasi.

## 4. Cara Menjalankan Aplikasi

### A. Menjalankan dari Kode Python

Pastikan MySQL aktif dan virtual environment sudah diaktifkan. Kemudian jalankan:

```powershell
python main.py
```

Jendela Login akan muncul. Masukkan username dan password akun yang sudah terdaftar pada tabel `users`.

Setelah login berhasil, pengguna akan diarahkan ke halaman pengelolaan buku sesuai perannya.

### B. Menjalankan Pengujian Otomatis

Untuk menjalankan seluruh pengujian:

```powershell
python -m pytest -v
```

Pengujian ini digunakan untuk memeriksa fungsi autentikasi dan pengelolaan data buku.

### C. Menjalankan Pemeriksaan Kualitas Kode

Jika Flake8 sudah terpasang, jalankan:

```powershell
python -m flake8 controllers models views config main.py
```

### D. Menjalankan Aplikasi Versi Executable

Aplikasi dapat dikemas menjadi file `.exe` menggunakan PyInstaller:

```powershell
python -m PyInstaller --onefile --windowed --name AplikasiPerpustakaan main.py
```

Jika proses berhasil, file aplikasi akan tersedia di:

```text
dist/AplikasiPerpustakaan.exe
```

Pastikan MySQL tetap berjalan dan konfigurasi database sesuai sebelum membuka aplikasi.

## 5. Otomasi CI Pipeline

Proyek menggunakan GitHub Actions untuk menjalankan pengujian otomatis ketika terdapat perubahan pada branch `main` atau pull request. Pipeline dapat digunakan untuk menginstal dependensi, memeriksa kualitas kode menggunakan Flake8, dan menjalankan pengujian otomatis menggunakan Pytest.
