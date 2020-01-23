import sqlite3 

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath) 

cur = conn.cursor()
cur.executescript("""
/* drop if a table exists */
DROP TABLE IF EXISTS items;

/* generate a table */
CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

/* put data inside the table */
INSERT INTO items (name, price) VALUES ('Apple', 12);
INSERT INTO items (name, price) VALUES ('Bananas', 9);
INSERT INTO items (name, price) VALUES ('Pepper', 32);
INSERT INTO items (name, price) VALUES ('Coffee', 10); """) 

# above manupulation to the databse
conn.commit()

# extract data 
cur = conn.cursor() 
cur.execute("SELECT item_id, name, price FROM items")
item_list = cur.fetchall() 

for i in item_list:
    print(i)