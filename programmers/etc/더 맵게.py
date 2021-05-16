import heapq


def solution(scoville, K):
    food = []
    res = 0
    for s in scoville:
        heapq.heappush(food, s)

    while len(food) > 1:
        first = heapq.heappop(food)
        second = heapq.heappop(food)
        if first >= K:
            break
        else:
            heapq.heappush(food, first + second * 2)
            res += 1

    if food and heapq.heappop(food) < K:
        return -1

    return res


solution([1, 2, 3, 9, 10, 12], 7)
