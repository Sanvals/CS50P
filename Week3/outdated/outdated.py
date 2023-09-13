months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        s = input("Date: ").strip()

        if "/" in s:
            try:
                data = s.split("/")
                y = data[2]
                m = int(data[0])
                d = int(data[1])

                if 1 < int(m) < 12 and 1 < int(d) < 31:
                    print(f"{y}-{m:02d}-{d:02d}")
                    break

            except ValueError:
                pass

        elif "," in s:
            try:
                data = s.split(" ")
                y = data[2]
                m = int(months.index(data[0])) +1
                d = int(data[1].strip(","))

                if 1 < int(m) < 12 and 1 < int(d) < 31:
                    print(f"{y}-{m:02d}-{d:02d}")
                    break

            except ValueError:
                pass

    except KeyError:
        pass