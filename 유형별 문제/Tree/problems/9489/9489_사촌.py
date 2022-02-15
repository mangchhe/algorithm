from collections import deque

input = __import__("sys").stdin.readline


def solve():

    q = deque([nums[0]])
    parent = {nums[0] : 0}
    level = {nums[0] : 0}
    levelCnt = 0
    cnt = 1
    now = 0

    for i in range(1, len(nums)):
        if q[-1] + 1 != nums[i]:
            cnt -= 1
            if cnt == 0:
                cnt = len(q)
                levelCnt += 1
            now = q.popleft()
        parent[nums[i]] = now
        level[nums[i]] = levelCnt
        q.append(nums[i])

    return len(list(filter(lambda x : parent[K] != parent[x[0]] and parent[parent[K]] == parent[parent[x[0]]], filter(lambda x: level[K] == x[1], level.items()))))

while True:

    N, K = map(int, input().split())

    if N == 0 and K == 0:
        break

    nums = list(map(int, input().split()))

    print(solve())
