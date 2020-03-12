from collections import deque

M, N = map(int, input().split())

tmp = deque(val for val in range(1, M + 1))

tmp2 = list(map(int, input().split()))

goal_val = 0
goal_idx = 0
count = 0

while len(tmp2):

    goal_val = tmp2.pop(0)
    goal_idx = tmp.index(goal_val)

    while True:
        if goal_val == tmp[0]:
            tmp.popleft()
            break
        if goal_idx > len(tmp) // 2:
            tmp.appendleft(tmp.pop())
            count += 1
        else:
            tmp.append(tmp.popleft())
            count += 1

print(count)