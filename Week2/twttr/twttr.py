ans = input("Input: ")

deliver = ""

vowels = ["a", "e", "i", "o", "u"]
for i in ans:
    if i.lower() not in vowels:
        deliver += i

print(deliver)