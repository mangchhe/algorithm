A = int(input())
B = input()

count = len(B)
sum = 0

for i in range(count):
    val = A*int(B[2-i])
    print(val)
    sum += val * 10**i

print(sum)