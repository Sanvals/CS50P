import random

while True:
    try:
        level = int(input("Level: "))

        if level > 0:
            break
        else:
            pass

    except ValueError:
        pass

find = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess == find:
            print("Just right!")
            break

        elif guess > find:
            print("Too large!")

        elif guess < find:
            if guess < 0:
                pass

            else:
                print("Too small!")

    except ValueError:
        pass