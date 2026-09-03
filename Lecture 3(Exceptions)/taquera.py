def main():
    select_items()

def select_items():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total_cost = 0
    while True:
        try:
            item = input("Item: ").strip().title()
            for key, value in menu.items():
                if item == key:
                    total_cost += value
                    print(f"${total_cost:.2f}")
        except EOFError:
            print("\n")
            break

main()