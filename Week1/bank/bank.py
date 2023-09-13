greet = input("Greeting: ").strip().lower()

print(greet[:4])
if greet[:5]== "hello":
    print ("$0")

elif greet[0] == "h":
    print("$20")

else:
    print("$100")