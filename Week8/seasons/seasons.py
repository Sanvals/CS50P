from datetime import date, timedelta
import inflect
import sys


def main():
    print(calculate(input("Date of Birth: ")))


def calculate(s):

    data = s.split("-")

    if len(data) != 3:
        print("Invalid Date")
        sys.exit(1)

    today = date.today()

    year = int(data[0])
    month = int(data[1])
    day = int(data[2])
    target = date(year, month, day)

    delta = today - target

    totalMinutes = delta.days * 24 * 60

    p = inflect.engine()

    return p.number_to_words(totalMinutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()