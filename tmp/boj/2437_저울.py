N = int(input())
weights = sorted(map(int, input().split()))
sumVal = 0

if weights[0] == 0:
    print(1)
    exit()

for weight in weights:
    if weight > sumVal + 1:
        break
    sumVal += weight

print(sumVal + 1)
