def main():
    # Requesting for user word
    statement = input("Input: ").strip()
    print(shorten(statement))


def shorten(words):
    vowels = ["A", "E", "I", "O", "U"]
    new_statement = ""
    for word in words:
        if word.upper() not in vowels:
            new_statement += word
    return new_statement

if __name__ == "__main__":
    main()