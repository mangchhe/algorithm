R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
ans = []

def find_row(x, y):
    s = ''
    for i in range(x, R):
        if arr[i][y] == '#':
            break
        s += arr[i][y]
    return s

def find_column(x, y):
    s = ''
    for i in range(y, C):
        if arr[x][i] == '#':
            break
        s += arr[x][i]
    return s

for i in range(R):
   s = find_column(i, 0)
   if len(s) >= 2:
       ans.append(s)

for i in range(C):
    s = find_row(0, i)
    if len(s) >= 2:
        ans.append(s)

for i in range(R):
    for j in range(C):
        if arr[i][j] == '#' and j + 1 < C:
            s = find_column(i, j + 1)
            if len(s) >= 2:
                ans.append(s)
        if arr[i][j] == '#' and i + 1 < R:
            s = find_row(i + 1, j)
            if len(s) >= 2:
                ans.append(s)

print(sorted(ans)[0])
