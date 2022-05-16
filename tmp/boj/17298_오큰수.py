N = int(input())
nums = list(map(int, input().split()))
s = [(nums[0], 0)]
ans = [-1] * N 

for i in range(1, N):
    if s[-1][0] > nums[i]:
        s.append((nums[i], i))
        continue

    while s and s[-1][0] < nums[i]:
        ans[s.pop()[1]] = nums[i]

    s.append((nums[i], i))

print(*ans)
