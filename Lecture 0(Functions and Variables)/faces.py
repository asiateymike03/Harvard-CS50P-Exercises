def main():
    # Asking user for input
    string = input("").strip()
    print(f"{convert(string)}")

def convert(words):
    word = words.replace(":)", "😊")
    word = word.replace(":(", "☹️")
    return word
    
main()
