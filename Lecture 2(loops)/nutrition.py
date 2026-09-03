# Asking uer for input
item = input("Item: ").strip().title()

# Fruits with calories
fruits = {
    15 : ["Lemon"],
    20 : ["Lime"],
    130 : ["Apple"],
    50 : ["Avocado", "Cantaloupe", "Honeydew Melon", "Pineapple", "Strawberries", "Tangerine"], 
    60 : ["Grapefruit", "Nectarine", "Peach"],
    70 : ["Plums"],
    80 : ["Orange", "Watermelon"],
    90 : ["Grape", "Kiwifruit"],
    100 : ["Pear", "Sweet Cherries"],
    110 : ["Banana"] 
}

for calorie, fruit in fruits.items():
    for available_fruit in fruit:
        if item in available_fruit:
            print(f"Calorie: {calorie}")
