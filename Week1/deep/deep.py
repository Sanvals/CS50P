answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
answer = answer.lower().strip()

choices = ["42", 42, "forty-two", "forty two"]

if answer in choices:
    print("Yes")
else:
    print("No")