def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Checking if all characters are alphanumeric
    if not s.isalnum():
        return False
    
    # Checking length of characters
    if len(s) < 2 and len(s) > 6:
        return False
   
    # Checking if characters starts with at least 2 characters
    if not s[:2].isalpha():
        return False

    for index,char in enumerate(s):
        if char.isdigit():
            num_index = index
            break

        if char.isalpha():
            char_index = (len(s) - index) - 1
            break

        if num_index > char_index:
            return True
        else:
            return False

main()