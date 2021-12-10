# 방법 1
N = 8
board = [list(input()) for _ in range(8)]
ans = 0

for i in range(N):
    n = 1 if i % 2 == 1 else 0
    for j in range(n, N, 2):
        if board[i][j] == 'F':
            ans += 1

print(ans)

# 방법 2
r = ''
for _ in range(8):
    r += input() + '0'
print(r[::2].count('F'))