
media = input("File name: ").lower()

if "." not in media:
    print("application/octet-stream")

else:

    media = media.strip().split(".")
    media = media[len(media) - 1]

    if media == "gif":
        print(f"image/gif")

    elif media == "jpg" or media == "jpeg":
        print(f"image/jpeg")

    elif media == "png":
        print(f"image/png")

    elif media == "pdf":
        print(f"application/pdf")

    elif media == "zip":
        print(f"application/zip")

    elif media == "txt":
        print(f"text/plain")

    else:
        print("application/octet-stream")
