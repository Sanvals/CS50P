from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()
modes = ["-f", "--font"]

argc = len(sys.argv)

if argc == 1:
    rand = random.randrange(0, len(fonts))
    figlet.setFont(font=fonts[rand])

    ans = input("Input: ")

    print("Output:")
    print(figlet.renderText(ans))

elif argc == 3:
    mode = sys.argv[1]
    font = sys.argv[2]

    if mode not in modes:
        print("Invalid usage")
        sys.exit(1)

    if font not in fonts:
        print("Invalid usage")
        sys.exit(1)


    figlet.setFont(font=font)

    ans = input("Input: ")

    print("Output:")
    print(figlet.renderText(ans))

else:
    print("Invalid usage")
    sys.exit(1)

