import sqlite3
Conn = sqlite3.connect("Data.db")
Cursor = Conn.cursor()

def Insert(Values):
   with Conn:
      Cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (Values[0],Values[1]))


def Reset():
   with Conn:
       try:
           Cursor.execute("SELECT MAX(id) FROM users")
           tablesize = Cursor.fetchone()
           maxsize = int(tablesize[0])
           for i in range(2, maxsize + 1):
               Cursor.execute("DELETE FROM users WHERE id = ?", (i,))
       except:
           print("Empty Table")

def UsernameFind(Value):
   with Conn:
       Cursor.execute("SELECT id FROM users WHERE username == ?", (Value,))
       val = Cursor.fetchone()
       return bool(val)


def PasswordFind(Value):
   with Conn:
       Cursor.execute("SELECT id FROM users WHERE password == ?", (Value,))
       val = Cursor.fetchone()
       return bool(val)

Reset()