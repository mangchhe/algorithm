import heapq

input = __import__("sys").stdin.readline

for _ in range(int(input())):
    N = int(input())
    files = list(map(int, input().split()))
    res = 0
    heapq.heapify(files)

    for i in range(N - 1):
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        heapq.heappush(files, a + b)
        res += a + b

    print(res)
