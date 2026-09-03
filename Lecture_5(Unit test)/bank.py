def main():
    greeting = input("Greeting: ").strip()
    print(value(greeting))


def value(greetings):
    if greetings.lower().startswith("hello"):
        return f"$0"
    elif greetings.lower().startswith("h") and not greetings.lower().startswith("hello"):
        return f"$20"
    else:
        return f"$100"


if __name__ == "__main__":
    main()