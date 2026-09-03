import random


def main():
    level = get_level()
    marks = 0
    for _ in range(10):
        x_value, y_value = generate_integer(level)
        correct_answer = int(x_value) + int(y_value)
        for attempt in range(3):
            try:    
                answer = int(input(f"{int(x_value)} + {int(y_value)} = "))
                if answer == correct_answer:
                    marks += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                pass
        else:        
            print(f"{int(x_value)} + {int(y_value)} = {int(x_value) + int(y_value)}")        
    print(f"Score: {marks}")


def get_level():
    #getting user input
    while True:
        lvl = int(input("Level: "))
        if lvl in [1,2,3]:
            return lvl 

def generate_integer(level):
    #evaluating digits based on input
    if level == 1:
        x = random.randint(1,9)
        y = random.randint(1,9)
        return x, y
    if level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return x, y
    if level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return x, y


if __name__ == "__main__":
    main()