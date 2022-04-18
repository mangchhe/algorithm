import heapq

N, M = map(int, input().split())
cards = list(map(int, input().split()))
h = []

heapq.heapify(cards)

for _ in range(M):
    _sum = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, _sum)
    heapq.heappush(cards, _sum)

print(sum(cards))
