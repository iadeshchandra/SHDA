import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("shda.db", check_same_thread=False)
        self.create()

    def create(self):
        c = self.conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS members(id INTEGER PRIMARY KEY, name TEXT, phone TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS donations(id INTEGER PRIMARY KEY, member_id INTEGER, amount REAL, date TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY, category TEXT, name TEXT, items TEXT, total REAL, date TEXT)")

        self.conn.commit()

    def add_member(self, name, phone):
        self.conn.execute("INSERT INTO members(name,phone) VALUES (?,?)",(name,phone))
        self.conn.commit()

    def get_members(self):
        return self.conn.execute("SELECT * FROM members").fetchall()

    def add_donation(self, member_id, amount):
        self.conn.execute("INSERT INTO donations(member_id,amount,date) VALUES (?,?,?)",(member_id,amount,str(datetime.now())))
        self.conn.commit()

    def add_expense(self, category, name, items, total):
        self.conn.execute("INSERT INTO expenses(category,name,items,total,date) VALUES (?,?,?,?,?)",
                          (category,name,items,total,str(datetime.now())))
        self.conn.commit()