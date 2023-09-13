import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    short = "https://youtu.be/"
    match = re.search(r"src=\"http[s]*://[www.]*youtube.com/embed/(?P<url>.+?)\"", s)

    if match is None:
        return None

    url = match["url"]

    return short + url

if __name__ == "__main__":
    main()