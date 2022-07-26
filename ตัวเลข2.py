"""ตัวเลขที่มีอยู่"""
def main():
    """"ตัวเลขที่มีอยู่"""
    leng = int(input())
    i = 0
    while True:
        if leng == 0:
            print("No Tape Measure")
            break
    for _ in range(leng):
        in1 = input().lower()
        if in1 != "no more" and in1 != 0 and in1 != "Not Found Number":
            in1 = int(in1)
            i = i+in1
        elif in1 == "Not Found Number":
            print("Not Found Number")
        elif in1 == "no more":
            break
        else:
            pass
    print("Sum of Found Number =", i)
main()
