grocery = {}

while True:
    try:
        item = input("")

        try:
            grocery[item] += 1

        except KeyError:
            grocery[item] = 1

    except ValueError:
        pass

    except EOFError:
        break


list = sorted(grocery)

for i in list:
    print(f"{grocery[i]} {i.upper()}")