def main():
    # Asking user for time
    recorded_time = input("What time is it? ").strip()
    if convert(recorded_time) >= 7 and convert(recorded_time) <= 8:
        print("breakfast time")
    elif convert(recorded_time) >= 12 and convert(recorded_time) <= 13:
        print("lunch time")
    elif convert(recorded_time) >= 18 and convert(recorded_time) <= 19:
        print("dinner time")
    

def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes)/ 60
    return float(hours) + minutes

if __name__ == "__main__":
    main()