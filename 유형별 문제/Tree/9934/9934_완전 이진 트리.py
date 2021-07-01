input = __import__("sys").stdin.readline

N = int(input())


def solve(arr, s, e, floor):
    if floor == N:
        return
    else:
        mid = (s + e) // 2
        ans[floor].append(arr[mid])

        solve(arr, s, mid - 1, floor + 1)
        solve(arr, mid + 1, e, floor + 1)


arr = list(map(int, input().split()))
ans = [[] for _ in range(N)]

solve(arr, 0, len(arr) - 1, 0)

for i in ans:
    print(" ".join(map(str, i)))
