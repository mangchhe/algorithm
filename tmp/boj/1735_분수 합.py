def uclid(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp

    return a

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

n = a1 * b2 + a2 * b1
d = b1 * b2
division = uclid(n, d)

print(n // division, d // division)
