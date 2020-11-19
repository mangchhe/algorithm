"""
    작성일 : 20/11/19

    url : https://programmers.co.kr/learn/courses/30/lessons/42889
"""

import heapq

def solution(N, stages):

    length = len(stages)
    stageCnt = [0 for i in range(N + 2)]
    stageHeap = []
    result = []

    for i in stages:
        stageCnt[i] += 1

    for i in range(1, N + 1):
        if stageCnt[i] != 0:
            heapq.heappush(stageHeap, (-(stageCnt[i] / length), i))
            length -= stageCnt[i]
        else:
            heapq.heappush(stageHeap, (0, i))

    while stageHeap:
        result.append(heapq.heappop(stageHeap)[1])

    return result

ex = [[5, [2, 1, 2, 6, 2, 4, 3, 3]], [4, [4,4,4,4,4]]]

for n, stages in ex:
    print(solution(n, stages))