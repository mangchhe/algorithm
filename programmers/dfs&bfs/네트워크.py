""" 
    작성일 : 20/09/14
"""

from collections import deque

def solution(n, computers):
    direction = {}
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if i not in direction:
                    direction[i]= [j]
                else:
                    direction[i].append(j)

    result = []

    while direction:
        tmp = list(direction.keys())[0]
        visited = [tmp]
        queue = deque(direction[tmp])
        del direction[tmp]

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.append(current)
                queue.extend(direction[current])
                del direction[current]

        result.append(visited)

    return len(result)

solution(3, [[1,1,0],[1,1,0],[0,0,1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])