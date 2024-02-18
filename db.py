import sqlite3

db = sqlite3.connect('Login.db')

cur = db.cursor()

# Comment this line if running for the first time or an exception will occur
cur.execute("DROP TABLE users")
cur.execute("DROP TABLE marks")

cur.execute("CREATE TABLE users(username TEXT,password TEXT)")
cur.execute("INSERT INTO users VALUES (?,?)",("harry","potter"))
cur.execute("INSERT INTO users VALUES (?,?)",("tom","cat"))
cur.execute("INSERT INTO users VALUES (?,?)",("jon","snow"))

cur.execute("SELECT * FROM users")
users = {}
[users.update({row[0]:row[1]}) for row in cur]


cur.execute("CREATE TABLE marks(username TEXT,test TEXT,math TEXT, english TEXT, science TEXT, history TEXT, geography TEXT)")

 
marks = [("tom",1,50,51,52,53,54),
         ("tom",2,60,61,62,63,64),
         ("harry",1,50,51,52,53,54),
         ("harry",2,60,61,62,63,64),
         ("harry",3,70,71,72,73,74),  
         ("jon",1,50,51,52,53,54),
         ("jon",2,60,61,62,63,64),
         ("jon",3,70,71,72,73,74),   
         ("jon",4,80,81,82,83,84) 
        ]

cur.executemany("INSERT INTO marks VALUES (?,?,?,?,?,?,?)",marks)


db.commit()
db.close()