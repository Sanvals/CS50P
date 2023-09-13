from validator_collection import validators, checkers, errors

def main():
    print(validate(input("What's your email adress? ")))


def validate(s):
    if checkers.is_email(s):
        value = "Valid"
    else:
        value = "Invalid"

    return value

if __name__ == "__main__":
    main()