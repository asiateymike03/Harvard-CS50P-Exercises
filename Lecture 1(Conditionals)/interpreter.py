def main():
    # Asking user for expression
    expression = input("Expression: ").strip()
    print(f"{eval(expression):.1f}")

def eval(input):
    exp = input.split(" ")
    if exp[1] == "+":
        return float(exp[0]) + float(exp[2])
    elif exp[1] == "-":
        return float(exp[0]) - float(exp[2])
    elif exp[1] == "/":
        return float(exp[0]) / float(exp[2])
    elif exp[1] == "*":
        return float(exp[0]) * float(exp[2])

main()