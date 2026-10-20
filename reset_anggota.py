from config.database import Database

db = Database()
conn = db.get_connection()

if conn:
    cursor = conn.cursor()

    cursor.execute("DELETE FROM anggota")
    conn.commit()

    print("Semua data anggota berhasil dihapus!")

    cursor.close()
    conn.close()