ans = input("camelCase: ")
result = ""
for i in ans:
    if i.isupper():
        result += "_" + i.lower()
    else:
        result += i

print(result)