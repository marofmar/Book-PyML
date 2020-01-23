import yaml 

# define YAML data
yaml_str = """
Date: 2020-01-22
PriceList: 
    -
        item_id: 1000
        name: Banana
        color: yellow
        taste: sweet
    -
        item_id: 1001
        name: Lemon
        color: yellow
        taste: sour 
    -
        item_id: 2001
        name: Pepper
        color: grayish black
        taste: spicy
"""

# analyze YAML
data = yaml.load(yaml_str)

# print out name and the flavor of it
for item in data['PriceList']:
    print(item['name'],"'s taste is", item['taste'])