N = int(input())

for _ in range(N):
    ans = ''
    S = input().split()
    for s in S:
        ans += s[::-1] + ' '
    print(ans)
