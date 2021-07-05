input = __import__("sys").stdin.readline

for _ in range(int(input())):
    N = int(input())
    parent = [0] * (N + 1)
    ans = 0
    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a

    A, B = map(int, input().split())
    parent_a = [0, A]
    parent_b = [0, B]

    while parent[A]:
        parent_a.append(parent[A])
        A = parent[A]
    while parent[B]:
        parent_b.append(parent[B])
        B = parent[B]

    idx = -1
    while parent_a[idx] == parent_b[idx]:
        ans = parent_a[idx]
        idx -= 1

    print(ans)
