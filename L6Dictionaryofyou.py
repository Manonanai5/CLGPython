my_info = {
    "name": "Sarah",
    "age": 39,
    "occupation": "Digital Strategy",
    "hobby": "Coding",
    "favorite_color": "Black"
}

for key, value in my_info.items():
    print(f"My {key} is {value}.")

my_info["favorite_food"] = "Tacos"
my_info["age"] = 39
del my_info["hobby"]
my_info.clear()

print("\nUpdated Dictionary:", my_info)