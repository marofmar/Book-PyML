import yaml
# print data in YAML format 

customer = [
    {"name": "Jenny", "age": "75", "job": "Accountant"},
    {"name": "Ahmed", "age": "21", "job": "Swimming instructor"},
    {"name": "Henry", "age": "36", "job": "Actor"}
]

yaml_str = yaml.dump(customer) 
print(yaml_str)
print("-- -- --")

# YAML into Python data
data = yaml.load(yaml_str) 
print(data)
# print the names 
for p in data:
    print(p['name'])  