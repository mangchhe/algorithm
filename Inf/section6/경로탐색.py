import sys

# sys.stdin = open('input.txt', 'rt')

def dfs(v):

    global cnt
    
    if v == n:
        cnt += 1
    else:
        for i, d in enumerate(data[v]):
            if i in visited:
                continue
            if d == 1:
                visited.append(i)
                dfs(i)
                visited.pop()
    
if __name__ == '__main__':
    
    n, m = map(int, input().split())

    data = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        data[x][y] = 1

    cnt = 0
    visited = [1]

    dfs(1)

    print(cnt)



