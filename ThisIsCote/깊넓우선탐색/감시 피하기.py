"""
    작성일 : 20/11/15
"""

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution():
    n = int(input())
    data = [input().split() for i in range(n)]
    blankSpace = []
    teacher = []

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                blankSpace.append((i, j))
            elif data[i][j] == 'T':
                teacher.append((i, j))

    length = len(blankSpace)

    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                x1, y1 = blankSpace[i] 
                x2, y2 = blankSpace[j] 
                x3, y3 = blankSpace[k] 
                data[x1][y1], data[x2][y2], data[x3][y3] = 'B', 'B', 'B'

                if searchStudent(data, teacher, n):
                    return True
                    
                data[x1][y1], data[x2][y2], data[x3][y3] = 'X', 'X', 'X'

    return False

def searchStudent(data, teacher, n):

    for t in teacher:
        for i in range(4):
            x, y = t
            while True:
                x = x + dx[i]
                y = y + dy[i]
                if x < n and x > -1 and y < n and y > -1:
                    if data[x][y] == 'B':
                        break
                    elif data[x][y] == 'S':
                        return False
                else:
                    break
    return True
                
if solution():
    print('YES')
else:
    print('NO')