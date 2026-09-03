def main():
    level = input("Fraction: ")
    gauge_lvl = convert(level)
    lvl = gauge(gauge_lvl)
    print(lvl)

def convert(fraction):
    values = fraction.split("/")
    try:
        numerator = int(values[0])
        denominator = int(values[1])
        if denominator == 0:
            raise ZeroDivisionError
        gauge = int((numerator/ denominator) * 100)
    except (ValueError, ZeroDivisionError):
        raise
    return gauge

def gauge(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()