import sys

if len(sys.argv) != 2:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments")

    sys.exit(1)

name = sys.argv[1]
score = 0

if name.split(".")[1] != "py":
    print("Not a Python file")
    sys.exit(1)

try:
    with open(name, "r") as file:
        lines = file.readlines()

    for line in lines:
        if not line.strip().startswith("#") and len(line.strip()) != 0:
            score += 1

    print(score)

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)