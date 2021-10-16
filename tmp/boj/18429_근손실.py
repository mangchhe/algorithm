# https://www.acmicpc.net/problem/18429

def traverse(n, weight):
    global ans
    if n == len(weights):
        ans += 1
        return
    else:
        for i in range(len(weights)):
            if not visited[i] and weight - K + weights[i] >= 500:
                visited[i] = 1
                traverse(n + 1, weight - K + weights[i])
                visited[i] = 0

N, K = map(int, input().split())
weights = list(map(int, input().split()))
visited = [0] * len(weights)
ans = 0

traverse(0, 500)

print(ans)
