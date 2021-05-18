import heapq


def solution(operations):

    heap = []

    for operation in operations:
        op, n = operation.split()
        if op == 'I':
            heapq.heappush(heap, int(n))
        elif op == 'D' and heap:
            if n == '1':
                # heap.remove(heapq.nlargest(1, heap)[0])
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)

    if len(heap) > 1:
        # return [heapq.nlargest(1, heap)[0], heapq.heappop(heap)]
        return [max(heap), heapq.heappop(heap)]
    elif len(heap) == 1:
        n = heapq.heappop()
        return [n, n]
    else:
        return [0, 0]


print(solution(["I 7", "I 5", "I -5", "D -1"]))
