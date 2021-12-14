from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        def move(x, y):
            yield x + 1, y
            yield x - 1, y
            yield x, y + 1
            yield x, y - 1
        
        n = len(maze)
        m = len(maze[0])
        visited = [[0] * m for _ in range(n)]
        visited[entrance[0]][entrance[1]] = 1
        q = deque([(entrance[0], entrance[1])])
        
        while q:
            x, y = q.popleft()
            if x == 0 or y == 0 or x == n - 1 or y == m - 1:
                if visited[x][y] != 1:
                    return visited[x][y] - 1
            for cx, cy in move(x, y):
                if cx < 0 or cx >= n or cy < 0 or cy >= m or visited[cx][cy]:
                    continue
                if maze[cx][cy] == '.':
                    visited[cx][cy] = visited[x][y] + 1
                    q.append((cx, cy))
                
        return -1
