due = 50

coins = [25, 10, 5]

while True:
    print(f"Amount Due: {due}")
    ans = int(input("Insert Coin: "))

    if ans in coins:
        due -= ans

    if due <= 0:
        print(f"Change Owed: {abs(due)}")
        break