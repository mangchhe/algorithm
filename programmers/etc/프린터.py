from collections import deque

# 방법 1
# def solution(priorities, location):

#     waitList = deque([])
#     res = 0

#     for i, prioritie in enumerate(priorities):
#         waitList.append([prioritie, i])

#     while True:
#         maxVal = max(list(zip(*waitList))[0])
#         tmp = waitList.popleft()
#         if tmp[0] != maxVal:
#             waitList.append(tmp)
#         else:
#             res += 1
#             if tmp[1] == location:
#                 break

#     return res


# 방법 2
def solution(priorities, location):

    queue = deque([])
    res = 0

    for i, prioritie in enumerate(priorities):
        queue.append([prioritie, i])

    while True:
        cur = queue.popleft()
        if any(cur[0] < q[0] for q in queue):
            queue.append(cur)
        else:
            res += 1
            if cur[1] == location:
                return res


solution([1, 1, 9, 1, 1, 1], 0)