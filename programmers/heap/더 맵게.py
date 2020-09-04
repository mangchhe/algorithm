""" 
    작성일 : 20/09/04
"""

""" def solution(scoville, K):

    count = 0

    while scoville[0] <= K:

        tmp = scoville[0] + (scoville[1] * 2)
        del scoville[0]
        del scoville[0]
        for i, j in enumerate(scoville):
            if tmp <= j:
                scoville.insert(i, tmp)
                break

        count += 1

    return count

print(solution([1, 2, 3, 9, 10, 12], 7)) """

import heapq

def solution(scoville, K):

    heapq.heapify(scoville)
    count = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)) 
        count += 1

    return count

print(solution([1], 7)) 