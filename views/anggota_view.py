import customtkinter as ctk
from tkinter import ttk


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Data Anggota Perpustakaan")
        self.geometry("900x500")

        # ================= FORM DATA ANGGOTA =================
        frame_kiri = ctk.CTkFrame(self)
        frame_kiri.pack(
            side="left",
            fill="both",
            expand=False,
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 16, "bold")
        ).pack(pady=20, padx=30)

        ctk.CTkLabel(
            frame_kiri,
            text="Nama Anggota"
        ).pack(pady=(10, 5))

        self.entry_nama = ctk.CTkEntry(
            frame_kiri,
            placeholder_text="Masukkan Nama Anggota",
            width=250
        )
        self.entry_nama.pack(pady=5, padx=20)

        ctk.CTkLabel(
            frame_kiri,
            text="Alamat"
        ).pack(pady=(15, 5))

        self.entry_alamat = ctk.CTkEntry(
            frame_kiri,
            placeholder_text="Masukkan Alamat",
            width=250
        )
        self.entry_alamat.pack(pady=5, padx=20)

        self.btn_simpan = ctk.CTkButton(
            frame_kiri,
            text="Simpan Data",
            fg_color="green",
            width=250,
            command=self.simpan_data
        )
        self.btn_simpan.pack(pady=25, padx=20)

        # ================= DAFTAR ANGGOTA =================
        frame_kanan = ctk.CTkFrame(self)
        frame_kanan.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            frame_kanan,
            text="Daftar Anggota Perpustakaan",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        ctk.CTkLabel(
            frame_kanan,
            text="Muhammad Fadhil Nasrullah | F5212530093",
            font=("Arial", 10, "bold")
        ).pack(pady=(0, 10))

        # ================= TABEL =================
        kolom = ("id", "nama", "alamat")

        self.tabel = ttk.Treeview(
            frame_kanan,
            columns=kolom,
            show="headings"
        )

        self.tabel.heading("id", text="ID Anggota")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        self.tabel.column(
            "id",
            width=100,
            anchor="center"
        )

        self.tabel.column(
            "nama",
            width=220
        )

        self.tabel.column(
            "alamat",
            width=250
        )

        self.tabel.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # ================= DATA CONTOH =================
        data_anggota = [
            (1, "Muhammad Sultan Raihan", "Jl. Anoa"),
            (2, "Samsul Qiran", "Jl. Kayumalue"),
            (3, "Muhammad Dzaky Kurniawan", "Jl. Thamrin"),
            (4, "Pasha Ahmad", "Jl. Tondo")
        ]

        for data in data_anggota:
            self.tabel.insert(
                "",
                "end",
                values=data
            )

    # ================= FUNGSI SIMPAN =================
    def simpan_data(self):
        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()

        if nama and alamat:
            id_baru = len(self.tabel.get_children()) + 1

            self.tabel.insert(
                "",
                "end",
                values=(id_baru, nama, alamat)
            )

            self.entry_nama.delete(0, "end")
            self.entry_alamat.delete(0, "end")


# ================= MENJALANKAN PROGRAM =================
if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()