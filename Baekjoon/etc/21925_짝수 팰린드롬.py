n = int(input())
arr = list(map(int, input().split()))
res = 0
tmp = []

for i in range(n):
    tmp.append(arr[i])
    if len(tmp) % 2 == 0:
        if tmp == tmp[::-1]:
            res += 1
            tmp = []

if tmp:
    print(-1)
else:
    print(res)
