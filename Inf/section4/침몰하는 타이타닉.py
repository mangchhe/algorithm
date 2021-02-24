import sys

# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
res = 0

while data:

    maxWei = 0
    removedArr = []
    cnt = 0

    for i in range(n):
        if maxWei + data[i] <= m:
            cnt += 1
            removedArr.append(i)
            maxWei += data[i]
        if cnt == 2:
            break
    
    for i in removedArr[::-1]:
        del data[i]
        n -= 1

    removedArr.clear()

    res += 1

print(res)