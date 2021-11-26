N = int(input())
num = 1

for i in range(2, N + 1):
    num *= i
    while num % 10 == 0:
        num //= 10
        num %= 10000000000

print(num % 10)
