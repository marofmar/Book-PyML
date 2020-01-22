import requests 
r = requests.get("https://thumbs.dreamstime.com/z/seoul-architecture-line-skyline-illustration-linear-vector-cityscape-famous-landmarks-city-sights-design-icons-seoul-101576349.jpg")

# save in binary format 
with open("test.jpg", "wb") as f:
    f.write(r.content) 

print("saved") 