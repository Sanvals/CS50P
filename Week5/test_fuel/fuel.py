def main():
    while True:
        fraction = input("Fraction: ")

        try:
            percent = convert(fraction)
            break

        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percent))


def convert(fraction):
    x = int(fraction.split("/")[0])
    y = int(fraction.split("/")[1])

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    else:
        return round(x/y * 100)


def gauge(percentage):
    if 100 >= percentage >= 99:
        return "F"

    elif percentage <= 1:
        return "E"

    else:
        return f"{str(percentage)}%"


if __name__ == "__main__":
    main()