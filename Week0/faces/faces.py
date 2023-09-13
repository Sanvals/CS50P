string = input("")

def putSmiley(string):
    modified = string.replace(":)", "🙂").replace(":(", "🙁 ")
    return modified

print(putSmiley(string))