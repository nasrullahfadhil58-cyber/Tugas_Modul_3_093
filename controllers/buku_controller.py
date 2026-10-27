
import tkinter.messagebox as messagebox

from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan role pengguna
        self.view.title(
            f"Sistem Manajemen Perpustakaan - "
            f"Mode: {self.user_role.upper()}"
        )

        # Menghubungkan tombol dengan fungsi
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_update.configure(
            command=self.perbarui_buku
        )
        self.view.btn_hapus.configure(
            command=self.hapus_buku
        )
        self.view.btn_logout.configure(
            command=self.logout
        )

        # Memilih data dari tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_buku
        )

        # Pembatasan akses untuk anggota
        if self.user_role != "admin":
            self.view.btn_simpan.configure(
                state="disabled",
                text="Khusus Admin"
            )
            self.view.btn_update.configure(
                state="disabled"
            )
            self.view.btn_hapus.configure(
                state="disabled"
            )

            self.view.entry_judul.configure(
                state="disabled"
            )
            self.view.entry_penulis.configure(
                state="disabled"
            )
            self.view.entry_tahun.configure(
                state="disabled"
            )

        self.muat_data_tabel()

    # Menampilkan data buku
    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    # Menyimpan data buku
    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin menambah data!"
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        try:
            if self.model.create_buku(
                judul, penulis, tahun
            ):
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil disimpan!"
                )
                self.kosongkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data buku gagal disimpan!"
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Memilih data dari tabel
    def pilih_buku(self, event=None):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        if not data:
            return

        # Aktifkan sementara kolom untuk mengisi data
        self.view.entry_judul.configure(state="normal")
        self.view.entry_penulis.configure(state="normal")
        self.view.entry_tahun.configure(state="normal")

        self.view.entry_judul.delete(0, "end")
        self.view.entry_judul.insert(0, data[1])

        self.view.entry_penulis.delete(0, "end")
        self.view.entry_penulis.insert(0, data[2])

        self.view.entry_tahun.delete(0, "end")
        self.view.entry_tahun.insert(0, data[3])

        # Anggota hanya dapat melihat data
        if self.user_role != "admin":
            self.view.entry_judul.configure(
                state="disabled"
            )
            self.view.entry_penulis.configure(
                state="disabled"
            )
            self.view.entry_tahun.configure(
                state="disabled"
            )

    # Memperbarui data buku
    def perbarui_buku(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin memperbarui data!"
            )
            return

        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin diperbarui!"
            )
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )
        id_buku = data[0]

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        try:
            berhasil = self.model.update_buku(
                id_buku, judul, penulis, tahun
            )

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil diperbarui!"
                )
                self.muat_data_tabel()
                self.kosongkan_form()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data buku gagal diperbarui!"
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Menghapus data buku
    def hapus_buku(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin menghapus data!"
            )
            return

        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin dihapus!"
            )
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )
        id_buku = data[0]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"Yakin ingin menghapus buku '{data[1]}'?"
        )

        if not konfirmasi:
            return

        try:
            berhasil = self.model.delete_buku(id_buku)

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil dihapus!"
                )
                self.muat_data_tabel()
                self.kosongkan_form()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data buku gagal dihapus!"
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Mengosongkan form
    def kosongkan_form(self):
        if self.user_role != "admin":
            return

        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

    # Logout dan kembali ke halaman login
    def logout(self):
        konfirmasi = messagebox.askyesno(
            "Konfirmasi Logout",
            "Apakah Anda yakin ingin logout?"
        )

        if not konfirmasi:
            return

        self.view.destroy()

        from controllers.auth_controller import AuthController

        login = AuthController()
        login.run()

    # Menjalankan aplikasi
    def run(self):
        self.view.mainloop()
