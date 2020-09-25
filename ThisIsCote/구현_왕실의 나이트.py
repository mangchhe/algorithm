"""
    작성일 : 20/09/25
"""

canMovePos = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1], [-1, -2], [1, -2]]

current = list(input())

row = int(current[1]) - 1
column = ord(current[0]) - 97

result = 0

for r, c in canMovePos:

    if row + r > -1 and row + r < 8 and column + c > -1 and column + c < 8:
        result += 1

print(result)