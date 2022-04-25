import sys
from collections import deque

input = sys.stdin.readline

def leftRotate(idx, direction):
    if idx < 1:
        return
    if gear[idx][2] != gear[idx + 1][6]:
        leftRotate(idx - 1, -direction)
        gear[idx].rotate(-direction)

def rightRotate(idx, direction):
    if idx > 4:
        return
    if gear[idx][6] != gear[idx - 1][2]:
        rightRotate(idx + 1, -direction)
        gear[idx].rotate(-direction)

gear = [[]]
for _ in range(4): gear.append(deque(map(int, list(input().rstrip()))))

for _ in range(int(input())):
    n, direction = map(int, input().split())
    
    leftRotate(n - 1, direction)
    rightRotate(n + 1, direction)
    gear[n].rotate(direction)

ans = 0
for i in range(1, 5):
    if gear[i][0] == 1:
        ans += 2 ** (i - 1)

print(ans)
