import sys

# sys.stdin = open('input.txt', 'rt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):

    global res

    if x == n - 1 and y == n - 1:
        res += 1
    else:
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if -1 < cx < n and -1 < cy < n:
                if visited[cx][cy] == 0 and data[cx][cy] == '0':
                    visited[cx][cy] = 1
                    dfs(cx, cy)
                    visited[cx][cy] = 0


if __name__ == '__main__':

    n = 7
    data = []
    res = 0
    visited = [[0] * n for i in range(n)]

    for i in range(n):
        data.append(list(input().split()))

    visited[0][0] = 1

    dfs(0, 0)

    print(res)