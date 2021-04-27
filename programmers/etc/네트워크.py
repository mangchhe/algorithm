from collections import deque


def bfs(x, y, n, computers):

    q = deque([[x, y]])

    while q:
        x, y = q.popleft()
        if computers[x][y] == 1:
            computers[x][y] = 0
            computers[y][x] = 0
            for i in range(n):
                if computers[x][i] == 1:
                    q.append([x, i])
                if computers[i][y] == 1:
                    q.append([y, i])


def solution(n, computers):
    answer = 0

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                bfs(i, j, n, computers)
                answer += 1

    for i in range(n):
        if computers[i][i] == 1:
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
