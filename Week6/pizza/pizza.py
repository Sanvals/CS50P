import sys
from tabulate import tabulate
import csv

argc = len(sys.argv)
if argc != 2:
    if argc < 2:
        print("Too few command-line arguments")

    else:
        print("Too many command-line arguments")

    sys.exit(1)

name = sys.argv[1]

if name.split(".")[1] != "csv":
    print("Not a CSV file")
    sys.exit(1)

menu = []

try:
    with open(name, "r") as file:
        lines = csv.reader(file)

        for row in lines:
            menu.append({"regular": row[0], "small": row[1], "large": row[2]})

    print (tabulate(menu, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)