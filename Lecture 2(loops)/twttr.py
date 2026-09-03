def main():
    # Vowels
    vowels = ["A", "E", "I", "O", "U"]
    # Requesting for user word
    statement = input("Input: ").strip()

    new_statement = ""
    for word in statement:
        if word.upper() not in vowels:
            new_statement += word
    print(new_statement)

main()