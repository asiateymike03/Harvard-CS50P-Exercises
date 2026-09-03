import csv
import sys

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments.")

if len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments.")

#details stores names and homes of students
new_details = []
try:
    # reading from csv file
    with open(sys.argv[1], "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            detail = {"name" : row['name'], "house" : row['house']}
            new_name = row['name'].split(",")
            last_name = new_name[0].strip()
            first_name = new_name[1].strip()
            new_detail = {"first": first_name, "last": last_name, "house": row['house']}
            new_details.append(new_detail)
        
    # writing back into csv file 
    with open("after.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in new_details:
            writer.writerow({
                "first": student['first'],
                "last" : student['last'],
                "house" : student['house']
            })
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


