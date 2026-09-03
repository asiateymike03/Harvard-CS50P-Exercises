from datetime import date
import inflect
import re
import sys
        
def main():
    # Asking user for input
    initial_date = input("Date of Birth: ")
    if matches := re.search(r'^(\d{1,4})-(\d{1,2})-(\d{1,2})$', initial_date):
        birth_date = list(matches.groups())
    else:
        sys.exit("Invalid Dates")
    print(validate_birthday(birth_date))

def validate_birthday(s):
    birthday = date(int(s[0]), int(s[1]), int(s[2]))
    current_date = date.today()
    days_between = (current_date - birthday).days
    # Converting days of minutes
    minutes = days_between * 24 * 60
    # changing into word format
    p = inflect.engine()
    days_words = p.number_to_words(minutes, andword="").capitalize()
    return days_words

if __name__ == "__main__":
    main()