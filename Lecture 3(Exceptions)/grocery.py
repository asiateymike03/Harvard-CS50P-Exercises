def main():
    grocery()

def grocery():
    grocery_list = {}
    count = 0 
    while True:
        try:
            # Asking user for grocery item
            item = input().strip().upper()
            grocery_list[item] = grocery_list.get(item, 0) + 1
        except EOFError:
            print("\n")
            break
    for keys, values in sorted(grocery_list.items()):
        print(f"{values} {keys}")

main()  