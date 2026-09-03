from validator_collection import validators, checkers, errors

def main():
    # Asking user for e-mail
    print(validate_email(input("Enter your e-mail address: ")))


def validate_email(email):
    # Validating user e-mail provided
    is_email_address = checkers.is_email(email)
    if is_email_address:
        return "Valid"
    else: 
        return "Invalid"


if __name__ == "__main__":
    main()