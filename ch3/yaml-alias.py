import yaml

yaml_str = """
breakfast_menu:
    - &food1 "Mini crabs"
    - &food2 "Corn flakes"
    - &food3 "beef"
    - &food4 "coffee"

# alias test 

breakfast_today:
    main: *food1 
    desert: *food4
"""

data = yaml.load(yaml_str) 

print("Main: ", data['breakfast_today']['main'])
print("Desert: ", data['breakfast_today']['desert'])