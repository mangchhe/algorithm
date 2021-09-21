# https://www.acmicpc.net/problem/2309

# 방법1
# combinations 순열 이용

from itertools import combinations

heights = [int(input()) for _ in range(9)]
ans = []

for i in combinations(heights, 7):
    if sum(i) == 100:
        ans = sorted(list(i))
        break

for i in ans:
    print(i)

# 방법2
# 재귀 이용

import copy

heights = [int(input()) for _ in range(9)]
visited = []
res = []

def traverse(n):

    global res

    if len(visited) == 7:
        if sum(visited) == 100:
            res = copy.copy(visited)
        return

    if n > 9:
        return
    else:
        for i in range(n, 9):
            visited.append(heights[i])
            traverse(i + 1)
            visited.pop()

traverse(0)

for i in sorted(res):
    print(i)

# 방법3
# for문 이용(전체 난쟁이 키의 합 -  두 명의 난쟁이)

heights = [int(input()) for _ in range(9)]
heightSum = sum(heights)
excludes = 0
flag = False

for i in range(8):
    for j in range(i + 1, 9):
        if heightSum - heights[i] - heights[j] == 100:
            excludes = {i, j}
            break
    if excludes:
        break

for i in sorted([heights[i] for i in {0, 1, 2, 3, 4, 5, 6, 7, 8} - excludes]):
    print(i)
