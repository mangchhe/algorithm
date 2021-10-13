# https://www.acmicpc.net/problem/19949

def traverse(n, score):
    global ans
    if 10 - n + score < 5:
        return
    if n == 10:
        if score >= 5:
            ans += 1
        return
    else:
        for i in range(1, 6):
            if visited[n - 2 : n].count(i) == 2:
                continue
            else:
                visited.append(i)
                traverse(n + 1, score + 1 if answers[n] == i else score)
                visited.pop()

answers = list(map(int, input().split()))
visited = []
ans = 0

traverse(0, 0)

print(ans)
