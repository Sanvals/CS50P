def main():
    ans = input("Input: ")
    print(shorten(ans))

def shorten(word):
    deliver = ""

    vowels = ["a", "e", "i", "o", "u"]
    for i in word:
        if i.lower() not in vowels:
            deliver += i

    return deliver


if __name__ == "__main__":
    main()