import json 
price = {
    "date": "2020-01-22",
    "price": {
        "Apple": 80,
        "Orange": 55,
        "Pepper": 123
    }
}

s = json.dumps(price)
print(s)