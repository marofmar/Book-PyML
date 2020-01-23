from tinydb import TinyDB, Query 

# connect database 
filepath = "test-tynydb.json"
db = TinyDB(filepath) 

# if one already exists, remove
db.purge_table('fruits')

# generate a table / extract 
table = db.table('fruits')

# input data into the table 
table.insert({'name':'Pepper', 'age': 1})
table.insert({'name': 'Mads', 'age': 2})
table.insert({'name': 'Innes', 'age':3})
print(table.all()) 

# extract certain types of data 
# search Pepper
Item = Query() 
res = table.search(Item.name == 'Pepper') 
print('Pepper is ', res[0]['age'],'-year-old.')

# certain condition satisfy
print("Age over 2: ")
res = table.search(Item.age >=2)

for i in res:
    print(" |",i['name'] , i['age'])