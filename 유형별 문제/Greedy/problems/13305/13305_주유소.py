input = __import__('sys').stdin.readline

MI = lambda : list(map(int, input().split()))

N = int(input())
distance = MI()
cost = MI()

ans = distance[0] * cost[0]
now_cost = cost[0]

for i in range(1, len(distance)):
    if now_cost > cost[i]:
        now_cost = cost[i]
        ans += distance[i] * now_cost
    else:
        ans += distance[i] * now_cost

print(ans)