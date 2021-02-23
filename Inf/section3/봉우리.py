n = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

data = []
res = 0

for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        for k in range(4):
            if i + dx[k] > -1 and i + dx[k] < n and j + dy[k] > -1 and j + dy[k] < n:    
                if data[i][j] <= data[i + dx[k]][j + dy[k]]:
                    break
        else:
            res += 1
    
print(res)