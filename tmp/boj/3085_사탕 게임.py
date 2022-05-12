import sys
input = sys.stdin.readline

def getEatCandy():
    ret = 0
    for i in range(N):
        cnt = 1
        for j in range(N - 1):
            if candy[i][j] == candy[i][j + 1]:
                cnt += 1
                ret = max(ret, cnt)
            else:
                cnt = 1
        
        cnt = 1
        for j in range(N - 1):
            if candy[j][i] == candy[j + 1][i]:
                cnt += 1
                ret = max(ret, cnt)
            else:
                cnt = 1
    
    return ret

def move(x, y):
    yield x + 1, y
    yield x, y + 1

N = int(input())
candy = [list(input().rstrip()) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        for cx, cy in move(i, j):
            if cx > N - 1 or cy > N - 1:
                continue
            candy[i][j], candy[cx][cy] = candy[cx][cy], candy[i][j]
            ans = max(ans, getEatCandy())
            candy[i][j], candy[cx][cy] = candy[cx][cy], candy[i][j]

print(ans)
