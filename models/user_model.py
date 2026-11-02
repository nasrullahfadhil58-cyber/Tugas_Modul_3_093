
import hashlib
from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    def register_user(self, username, password, role):
        if not self.conn:
            return False

        cursor = self.conn.cursor()

        try:
            password_hash = self.hash_password(password)

            query = """
                INSERT INTO users (username, password, role)
                VALUES (%s, %s, %s)
            """

            cursor.execute(
                query, (username, password_hash, role)
            )
            self.conn.commit()
            return True

        except Exception as e:
            self.conn.rollback()
            print("Gagal mendaftarkan pengguna:", e)
            return False

        finally:
            cursor.close()

    def autentikasi(self, username, password):
        if not self.conn:
            return None

        cursor = self.conn.cursor(dictionary=True)

        try:
            password_hash = self.hash_password(password)

            query = """
                SELECT id_user, username, role
                FROM users
                WHERE username = %s AND password = %s
            """

            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()

            return user

        except Exception as e:
            print("Kesalahan autentikasi:", e)
            return None

        finally:
            cursor.close()
