""" 
    작성일 : 20/09/24
"""

n = int(input())
moveData = input().split()
directionData = {'L':[0, -1], 'R':[0, 1], 'U':[-1, 0], 'D':[1, 0]}
nowX = 0
nowY = 0

for data in moveData:

    x, y = directionData[data]

    if nowX + x > -1 and nowX + x < n and nowY + y > -1 and nowY + y < n:
        nowX += x
        nowY += y
    
print(nowX + 1, nowY + 1)