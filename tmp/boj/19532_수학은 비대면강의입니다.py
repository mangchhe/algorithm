a, b, c, d, e, f = map(int, input().split())

# 완탐
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            exit()

# 가감법
x = ((c * e) - (b * f)) // ((a * e) - (b * d))
y = ((c * d) - (a * f)) // ((b * d) - (a * e))
print(x, y)
