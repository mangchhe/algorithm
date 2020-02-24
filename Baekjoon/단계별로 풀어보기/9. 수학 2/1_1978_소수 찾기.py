N = int(input())

NList = list(map(int,input().split()))

count = 0

for i in NList:
    for j in range(2,i+1):
        if i == 1:
            break
        if i / j == 1:
            count += 1
            break
        if i % j == 0:
            break

print(count)