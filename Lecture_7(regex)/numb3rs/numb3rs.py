import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_numbers = []
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        ip_numbers = list(matches.groups())

        for number in ip_numbers:
            if len(number) > 1 and number.startswith("0"):
                return False
            
        for number in ip_numbers:
            if int(number) > 255:
                return False
        return True
    else:
        return False
        

if __name__ == "__main__":
    main()