import sqlite3

conn=sqlite3.connect("database.db")

print("opened db success")

conn.execute("CREATE TABLE UserEvents(id INTEGER PRIMARY KEY AUTOINCREMENT,uid INTEGER NOT NULL,EventName TEXT NOT NULL,occurence TEXT CHECK(occurence IN ('WEEKLY','MONTHLY','YEARLY')) NOT NULL,StartDate INTEGER NOT NULL,EndDate  INTEGER NOT NULL )")

print("table-2 created successfully")

conn.close()