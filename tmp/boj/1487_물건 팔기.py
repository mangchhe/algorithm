N = int(input())
arr = sorted(tuple(map(int, input().split())) for _ in range(N))
ans_benefit = 0
ans = 0

for i in range(N):
    total = 0
    for j in range(i, N):
        benefit = arr[i][0] - arr[j][1]
        if benefit < 0:
            continue

        total += benefit
    
    if ans_benefit < total:
        ans_benefit = total
        ans = arr[i][0]

print(ans)
