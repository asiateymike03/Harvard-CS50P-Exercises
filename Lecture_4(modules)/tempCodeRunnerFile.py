try:
        while True:
            l = int(input("Level: "))
            if l >= 1:
                #r represents random selection
                r = random.randint(1, l)
                return r
    except ValueError:
        pass