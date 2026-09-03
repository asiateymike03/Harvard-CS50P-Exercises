import sys

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments.")

if len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments.")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

lines = []
try:
    with open(sys.argv[1]) as file:
       for line in file:
           lines.append(line.strip())
except FileNotFoundError:
    sys.exit("File does not exist")

count = len(lines)

for line in lines:
    if line.startswith("#") or line == "":
        count -= 1
print(count)