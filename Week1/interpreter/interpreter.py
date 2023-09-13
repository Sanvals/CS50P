ans = input("Expression: ").split(" ")

x = int(ans[0])

y = ans[1]

z = int(ans[2])

if y == "+":
    answer = float(x + z)
    print("{:.1f}".format(answer))

elif y == "-":
    answer = float(x - z)
    print("{:.1f}".format(answer))

elif y == "*":
    answer = float(x * z)
    print("{:.1f}".format(answer))

elif y == "/":
    answer = float(x / z)
    print("{:.1f}".format(answer))