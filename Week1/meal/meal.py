def main():
    ans = input("What time is it? ")

    time = convert(ans)

    if time >= 7.0 and time < 8.0:
        print("breakfast time")
    elif time > 12.0 and time <= 13.0:
        print("lunch time")
    elif time > 18.0 and time < 19.0:
        print("dinner time")


def convert(time):
    hour = int(time.split(":")[0])
    min = int(time.split(":")[1])

    min = float(int(min) * 10 / 60) / 10

    return hour + min


if __name__ == "__main__":
    main()