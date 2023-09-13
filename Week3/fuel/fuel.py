def main():
    fuel = get_string()

    if 100 >= fuel >= 99:
        print("F")

    elif fuel <= 1:
        print("E")

    else:
        print(f"{fuel}%")


def get_string():
    while True:
        try:
            ans = input("Fraction: ")
            x = int(ans.split("/")[0])
            y = int(ans.split("/")[1])

            if x > y:
                pass

            else:
                return round(x/y * 100)

        except (ZeroDivisionError, ValueError):
            pass

main()