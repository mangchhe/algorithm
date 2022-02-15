import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(now):
    for n in st[now]:
        if visited[n]: continue
        visited[n] = 1
        if not book[n] or dfs(book[n]):
            book[n] = now
            return 1

    return 0

if __name__ == '__main__':
    for _ in range(int(input())):
        N, M = map(int, input().split())
        st = [[],]
        for _ in range(M):
            a, b = map(int, input().split())
            st.append(list(range(a, b + 1)))
        book = [0] * (N + 1)
        visited = []
        res = 0

        for i in range(1, M + 1):
            visited = [0] * (N + 1)
            if dfs(i):
                res += 1

        print(res)
