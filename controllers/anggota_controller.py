import sys
from pathlib import Path
from tkinter import messagebox

# Menambahkan folder utama proyek ke jalur pencarian Python
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Menghubungkan tombol Simpan dengan fungsi controller
        self.view.btn_simpan.configure(
            command=self.simpan_anggota
        )

        # Menampilkan data anggota pada tabel
        self.load_data()

    def load_data(self):
        # Mengambil data dari model
        data_anggota = self.model.get_all_anggota()

        # Menghapus data lama dari tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Memasukkan data anggota ke tabel
        for anggota in data_anggota:
            if isinstance(anggota, dict):
                nilai = (
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
                )
            else:
                nilai = anggota

            self.view.tabel.insert(
                "",
                "end",
                values=nilai
            )

    def simpan_anggota(self):
        # Mengambil nilai dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        # Memeriksa input
        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi."
            )
            return

        try:
            # Menyimpan data melalui model
            hasil = self.model.create_anggota(nama, alamat)

            if hasil is False:
                messagebox.showerror(
                    "Gagal",
                    "Data anggota gagal disimpan."
                )
                return

            # Memperbarui tabel setelah data disimpan
            self.load_data()

            # Mengosongkan form
            self.view.entry_nama.delete(0, "end")
            self.view.entry_alamat.delete(0, "end")

            messagebox.showinfo(
                "Berhasil",
                "Data anggota berhasil disimpan."
            )

        except Exception as error:
            messagebox.showerror(
                "Kesalahan",
                f"Gagal menyimpan data: {error}"
            )

    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    app = AnggotaController()
    app.run()