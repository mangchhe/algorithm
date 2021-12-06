# 첫 번째 방법
# import heapq
# from collections import defaultdict

# N, L = map(int, input().split())
# arr = list(map(int, input().split()))
# h = [arr[0]]
# check = defaultdict(int)
# check[arr[0]] = 1
# ans = []

# l, r = 0, 0

# while l <= N and r <= N:
#     if r - l < L - 1:
#         ans.append(h[0])
#         r += 1
#         check[arr[r]] += 1
#         heapq.heappush(h, arr[r])
#         continue
#     while not check[h[0]]:
#         heapq.heappop(h)

#     ans.append(h[0])

#     check[arr[l]] -= 1

#     if r + 1 >= N:
#         break

#     l, r = l + 1, r + 1
#     check[arr[r]] += 1
#     heapq.heappush(h, arr[r])

# print(*ans)

# 두 번째 방법
# deque 자료구조 이용 (value, idx) pair 저장
# 범위를 넘어서면 popleft 현재 범위 내에 최소 값만 보유 pop
from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()
ans = []

for i in range(N):
    n = arr[i]
    while q and q[0][1] < i - L + 1:
        q.popleft()
    while q and q[-1][0] >= n:
        q.pop()

    q.append((n, i))
    ans.append(q[0][0])

print(*ans)