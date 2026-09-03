import re
import sys

def main():
    # Asking user for time for conversion
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2})(?::(\d{1,2}))? (AM|PM) to (\d{1,2})(?::(\d{1,2}))? (AM|PM)$", s):
        start_hour = int(matches.group(1))
        start_minutes = int(matches.group(2) or 0)
        end_hour = int(matches.group(4))
        end_minutes = int(matches.group(5) or 0)

        # Validating first time
        if matches.group(3) == "PM" and 1 <= start_hour <= 11:
            if 0 <= start_minutes <= 59:
                start_hour += 12
                return f"{start_hour:02}:{start_minutes:02} to {end_hour:02}:{end_minutes:02}"
            elif matches.group(2)  is None:
                return f"{start_hour:02}:{0:02} to {end_hour:02}:{end_minutes:02}"
        elif matches.group(3) == "AM" and start_hour == 12:
            if 0 <= start_minutes <= 59:
                return f"{0:02}:{start_minutes:02} to {end_hour:02}:{end_minutes:02}"  
        else:
            raise ValueError("Invalid date or format")

    # Validating 2nd time
        if matches.group(6) == "PM" and 1 <= end_hour <= 11:
            if 0 <= end_minutes <= 59:
                end_hour += 12
                return f"{start_hour:02}:{start_minutes:02} to {end_hour:02}:{end_minutes:02}"
            elif matches.group(5) is None:
                return f"{start_hour:02}:{start_minutes:02} to {end_hour:02}:{0:02}"
        elif matches.group(6) == "AM" and end_hour == 12:
            if 0 <= end_minutes <= 59:
                return f"{start_hour:02}:{start_minutes:02} to {0:02}:{end_minutes:02}" 
        else:
            raise ValueError("Invalid date or format")
    else:
        raise ValueError("Invalid date or format")
                  
        
if __name__ == "__main__":
    main()