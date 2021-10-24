# https://www.acmicpc.net/problem/1895

R, C = map(int, input().split())
pixels = [list(map(int, input().split())) for _ in range(R)]
T = int(input())
ans = 0

def solve(x, y):
    arr = []
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            arr.append(pixels[i][j])
            
    return sorted(arr)[len(arr) // 2] >= T

for i in range(R - 2):
    for j in range(C - 2):
        ans += 1 if solve(i, j) else 0

print(ans)
