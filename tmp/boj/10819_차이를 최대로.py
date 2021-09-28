# https://www.acmicpc.net/problem/10819

input = __import__('sys').stdin.readline

N = int(input())
nList = list(map(int, input().split()))
visited = {}
ans = 0

def traverse(arr):
    global ans
    if len(arr) == N:
        total = 0
        for i in range(N - 1):
            total += abs(arr[i] - arr[i + 1])
        ans = max(ans, total)
    else:
        for i in range(N):
            if visited[nList[i]]:
                visited[nList[i]] -= 1
                arr.append(nList[i])
                traverse(arr)
                arr.pop()
                visited[nList[i]] += 1

for n in nList:
    if not visited.get(n):
        visited[n] = 1
    else:
        visited[n] += 1

traverse([])

print(ans)
