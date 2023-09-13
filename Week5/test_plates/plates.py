def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Check the letters
    if not s[:2].isalpha():
        return False

    # Check the length
    if len(s) not in range(2, 7):
        return False

    # Check special characters
    marks = [".", " ", "!", "?"]
    for i in s:
        if i in marks:
            return False

    # Check that there's no numbers followed by letters
    for i in range(len(s) - 1):
        if (s[i].isnumeric() and s[i + 1].isalpha()):
            return False

    # Check if 0 is the first digit
    for i in range(len(s) - 1):
        if (s[i].isalpha() and s[i + 1] == "0"):
            return False

    return True

if __name__ == "__main__":
    main()