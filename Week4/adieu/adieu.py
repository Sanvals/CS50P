names = []

while True:
    try:
        ans = input("Name: ")
        names.append(ans)

    except EOFError:
        break

print()

print("Adieu, adieu, to ", end="")

if len(names) == 1:
    print (names[0])
elif len(names) == 2:
    print(f"{names[0]} and {names[1]}")
else:
    for i in range(len(names) - 2):
        print(f"{names[i]}, ", end="")

    print(f"{names[len(names) - 2]}, and {names[len(names) - 1]}")