while 1:
    a, b = map(int, input().split())
    if a < 1 and b < 1:
        break
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
