def main():
    outdated_date()

def outdated_date():
    month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    new_date = ""
    while True:
        try:
            date = input().strip().title()
            for _ in date:
                if "/" in date:
                    sections = date.split("/")
                    month = int(sections[0])
                    day = int(sections[1])
                    if (month >= 1 and month <= 12) and (day >= 1 and day <= 31):
                        new_date = f"{sections[2]}-{month:02}-{day:02}"
                        print(new_date)
                        return
                    elif (month >= 1 and month <= 9) and (day >= 1 and day <= 9):
                        new_date = f"{sections[2]}-{month:02}{day:02}"
                        print(new_date)
                        return
                elif " " or "," in date:
                    sections = date.split(" ") and date.split(",")
                    month_day, year = date.split(",")
                    month, day = month_day.split()
                    day = int(day)
                    if (month in month_list) and (day >= 1 and day <= 31):
                        new_date = f"{year.strip()}-{month_list.index(month) + 1:02}-{day:02}"
                        print(new_date)
                        return
                    elif (month in month_list) and (day >= 1 and day <= 9):
                        new_date = f"{year.strip()}-{month_list.index(month) + 1:02}-{day:02}"
                        print(new_date)
                        return
        except ValueError:
            pass

main()