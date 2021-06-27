import heapq

input = __import__("sys").stdin.readline

h = []

for _ in range(int(input())):

    n = int(input())

    if n == 0:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        heapq.heappush(h, [abs(n), n])
