"""
    작성일 : 20/10/21
"""

dx = [0, -1, 1]
dy = [1, 1, 1]

def solve(data, n, m, result):
    for i in range(m):
        for j in range(n):
            for k in range(3):
                cx = j + dx[k]
                cy = i + dy[k]
                if cx > -1 and cy > -1 and cx < n and cy < m:
                    pass
                else:
                    break
                if result[cx][cy] < result[j][i] + data[cx][cy]:
                    result[cx][cy] = result[j][i] + data[cx][cy]
    gm = 0
    for i in range(n):
        if gm < result[i][m-1]:
            gm = result[i][m-1]
    
    return gm

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    data = []
    for i in range(n):
        data.append(tmp[m*i:m*(i+1)])
    result = [[0] * m for i in range(n)]
    for i in range(n):
        result[i][0] = data[i][0]

    print(solve(data, n, m, result))


