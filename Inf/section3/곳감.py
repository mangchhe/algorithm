n = int(input())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(int(input())):
    r, d, c = map(int, input().split())

    tmpArr = data[r - 1]
    
    if d == 0:
        for _ in range(c):
            tmpArr.append(tmpArr[0])
            del tmpArr[0]
    else:
        for _ in range(c):
            tmpArr.insert(0, tmpArr[-1])
            del tmpArr[-1]

    data[r - 1] = tmpArr

s, e = 0, n
res = 0

for i in range(n):
    for j in range(s, e):
        res += data[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)