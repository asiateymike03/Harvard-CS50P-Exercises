def main():
   # Asking user for name
    camel_case = input("camelCase: ") 
    print(f"snake_case: {snake_case(camel_case)}")

# Evaluating name
def snake_case(name):
    snake_case =""
    for n in name:
        if n.isupper():
            snake_case += "_" + n.lower()
        else:
            snake_case += n
    return snake_case

main()

