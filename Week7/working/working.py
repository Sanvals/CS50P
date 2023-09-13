import re


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if "-" in s:
        raise ValueError("ValueError")

    match = re.findall(r"(\d{1,2})( |:)(|\d{1,2})( |)(AM|PM)", s)

    if len(match) != 2:
        raise ValueError("Invalid input format")

    first_hour = match[0][0]
    first_minute = match[0][2]
    first_time = match[0][4]
    second_hour = match[1][0]
    second_minute = match[1][2]
    second_time = match[1][4]

    matchRe = [[first_hour, first_minute, first_time], [second_hour, second_minute, second_time]]

    for i in range(len(matchRe)):
        if matchRe[i][1] == '':
            matchRe[i][1] = "0"

        if int(matchRe[i][1]) > 59:
            raise ValueError("ValueError")

        if "PM" in matchRe[i]:
            matchRe[i][0] = str(int(matchRe[i][0]) + 12)
            if matchRe[i][0] == "24":
                matchRe[i][0] = "12"

        if "AM" in matchRe[i] and matchRe[i][0] == "12":
            matchRe[i][0] = "00"

    return f"{int(matchRe[0][0]):02d}:{int(matchRe[0][1]):02d} to {int(matchRe[1][0]):02d}:{int(matchRe[1][1]):02d}"

if __name__ == "__main__":
    main()
