import sys
import csv
import json

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments")

    sys.exit(1)

name = sys.argv[1]
score = 0

if name.split(".")[1] != "csv":
    print("Not a CSV file")
    sys.exit(1)

before = sys.argv[1]
after = sys.argv[2]

if before.split(".")[1] != "csv" or after.split(".")[1] != "csv":
    print("Not a CSV file")
    sys.exit(1)

data = []

try:
    with open(before, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            first = row[0].split(", ")[1]
            last = row[0].split(", ")[0]
            house = row[1]
            data.append({"first": first, "last": last, "house": house})


except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)


with open(after, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writerow({"first": "first", "last": "last", "house": "house"})

    for i in data:
        writer.writerow({"first": i["first"], "last": i["last"], "house": i["house"]})