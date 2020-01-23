import sqlite3
filepath = "test2.sqlite"
conn = sqlite3.connect(filepath)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items") 
cur.execute("""CREATE TABLE items (item_id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    price INTEGER)""")
conn.commit() 

# insert data
cur = conn.cursor() 
cur.execute(
    "INSERT INTO items (name, price) VALUES (?,?)",
    ("Orange", 23)
)
conn.commit() 

# insert many data 
cur = conn.cursor() 
data = [ ("Cider", 2), ("Brocoli",3), ("Cheese", 5)]
cur.executemany(
    "INSERT INTO items(name, price) VALUES (?,?)", data
)
conn.commit() 

# extract data that satiesfies certain range condition 
cur = conn.cursor()
price_range = (2,6)
cur.execute(
    "SELECT * FROM items WHERE price>=? AND price<=?", price_range
)
fetched_list = cur.fetchall()
for i in fetched_list:
    print(i)