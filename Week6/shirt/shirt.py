import sys
from PIL import Image, ImageOps

def main():
    argc = len(sys.argv)

    if argc < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    elif argc > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    else:
        program, before, after = sys.argv

        if before.split(".")[1] != after.split(".")[1]:
            print("Input and output have different extensions")
            sys.exit(1)

        edit(before, after)

def edit(before, after):
    try:
        shirt = Image.open("shirt.png")
        inputImage = Image.open(before)

        result = ImageOps.fit(inputImage, shirt.size)
        result.paste(shirt, shirt)
        result.save(after)

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


main()