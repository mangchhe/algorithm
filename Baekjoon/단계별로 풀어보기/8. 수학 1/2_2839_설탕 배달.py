N = int(input())

pkg3 = 0
pkg5 = 0

while N != 0:
    if N >= 5:
        N -= 5
        pkg5 += 1
    elif N >= 3:
        N -= 3
        pkg3 += 1
    else:
        if pkg5 > 0:
            N += 2
            pkg3 += 1
            pkg5 -= 1
        else:
            pkg3 = -1
            pkg5 = 0
            break

print(pkg3 + pkg5)
