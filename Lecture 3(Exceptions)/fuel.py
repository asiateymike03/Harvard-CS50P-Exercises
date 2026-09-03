while True:
    try:
        level = input("Fraction: ")
        values = level.split("/")

        numerator = int(values[0])
        denominator = int(values[1])

        gauge = int((numerator/ denominator) * 100)
        if gauge <= 1:
            print("E")
            break
        elif gauge >= 99:
            print("F")
            break
        else:
            print(f"{gauge}%")
            break
    except (ValueError, ZeroDivisionError):
        pass