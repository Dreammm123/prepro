"""d"""
def main():
    """d"""
    text = input()
    for i in text:
        if i.islower():
            print(chr(((122-(ord(i)-97)))), end="")
        elif i.isupper():
            print(chr(((90-(ord(i)-65)))), end="")
        else:
            print(i, end="")
main()
