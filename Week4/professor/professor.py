import random


def main():
    level = get_level()
    score = 0
    tries = 0


    for i in range(1, 11):
        tries = 0
        x = generate_integer(level)
        y = generate_integer(level)

        while True:

            guess = input(f"{x} + {y} = ")

            if int(guess) == (x + y):
                score += 1
                break
            else:
                print("EEE")
                if tries == 2:
                    print(f"{x} + {y} = {x + y}")
                    break
                else:
                    tries += 1


    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level not in range(1, 4):
                pass

            else:
                break

        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        return random.randint(0, 10)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()