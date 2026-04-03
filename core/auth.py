import hashlib
from core.database import Database

db = Database()

class Auth:
    def hash(self, p):
        return hashlib.sha256(p.encode()).hexdigest()

    def create_admin(self):
        c = db.conn.cursor()
        c.execute("SELECT * FROM users")
        if not c.fetchone():
            c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
            c.execute("INSERT INTO users(username,password) VALUES (?,?)",
                      ("admin", self.hash("admin123")))
            db.conn.commit()

    def login(self, u, p):
        c = db.conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?",
                  (u, self.hash(p)))
        return c.fetchone()