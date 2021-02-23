import sys

# sys.stdin = open('input.txt', 'rt')

data = []

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]

res = "YES"

for i in range(9):
    data.append(list(map(int, input().split())))

for i in range(9):
    tmpArr = [0 for i in range(9)]
    for j in range(9):
        if tmpArr[data[i][j] - 1] != 1:
            tmpArr[data[i][j] - 1] += 1
        else:
            res = "NO"
            break

for i in range(1, 9, 3):
    for j in range(1, 9, 3):
        tmpArr =  [0 for i in range(9)]
        tmpArr[data[i][j] - 1] += 1
        for k in range(8):
            if tmpArr[data[i + dx[k]][j + dy[k]] - 1] != 1:
                tmpArr[data[i + dx[k]][j + dy[k]] - 1] += 1
            else:
                res = "NO"
                break
        
print(res)