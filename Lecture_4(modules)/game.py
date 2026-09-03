import random

def main():
    level_num = level()
    guess_level = guess()
    if guess_level < level_num:
        print("Too small!")
        main()
    elif guess_level > level_num:
        print("Too large!")
        main()
    else:
        print("Just right!")

def level():
    while True:
        try:  
            l = int(input("Level: ").strip())
            if l >= 1:
                #r represents random selection
                r = random.randint(1, l)
                return r
        except ValueError:
            pass

def guess():
    while True:
        try: 
            
            g = int(input("Guess: ").strip())
            if g >= 1:
                return g
        except ValueError:
            pass

main()
