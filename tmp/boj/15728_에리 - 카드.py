N, K = map(int, input().split())
share_cards = list(map(int, input().split()))
team_cards = list(map(int, input().split()))
visited = [0] * N
ans = -float('INF')

for k in range(K):
    idx, n = 0, -float('INF')
    for i in range(N):
        for j in range(N):
            if not visited[i]:
                if share_cards[j] * team_cards[i] > n:
                    idx = i
                    n = share_cards[j] * team_cards[i]
            else:
                break

    visited[idx] = 1

for i in range(N):
    for j in range(N):
        if not visited[i]:
            ans = max(ans, share_cards[j] * team_cards[i])
        else:
            break

print(ans)
