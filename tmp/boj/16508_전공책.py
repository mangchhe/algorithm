input = __import__('sys').stdin.readline

def traverse(n, money):
    global ans
    if ans < money:
        return
    if len(list(filter(lambda x: x < 1, T.values()))) == M:
        ans = money
        return
    if n >= N:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            for t in T:
                T[t] -= books[i][1][t]
            traverse(n + 1, money + books[i][0])
            visited[i] = 0
            for t in T:
                T[t] += books[i][1][t]

s = input().rstrip()
T = {}

for i in s:
    T[ord(i) - 65] = T.get(ord(i) - 65, 0) + 1

books = []

for _ in range(int(input())):
    money, title = input().split()
    books.append((int(money), [0] * 26))
    for t in title:
        books[-1][1][ord(t) - 65] += 1
    if not books[-1][1]:
        books.pop()

N, M = len(books), len(T)
visited = [0] * N
ans = float('INF')

traverse(0, 0)

if ans == float('INF'):
    print(-1)
else:
    print(ans)
