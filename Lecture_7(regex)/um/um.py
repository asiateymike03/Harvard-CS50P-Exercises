import re
import sys


def main():
    # Asking user for text
    print(count(input("Text: ")))


def count(s):
    # Evaluating um based on string given
    pattern = re.findall(r'\bum', s, re.IGNORECASE)
    return len(pattern)


if __name__ == "__main__":
    main()