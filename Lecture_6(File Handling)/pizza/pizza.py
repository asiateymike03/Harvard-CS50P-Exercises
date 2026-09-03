import csv
import sys
from tabulate import tabulate

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments.")

if len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments.")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

pizzas = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        pizzas = list(reader)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(pizzas, headers="keys", tablefmt="grid"))
