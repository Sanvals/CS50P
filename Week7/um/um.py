import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"(^|\W)um($|\W)", s, re.IGNORECASE)
    counter = len(match)

    return counter


if __name__ == "__main__":
    main()