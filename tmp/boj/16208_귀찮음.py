N = int(input())
nList = sorted(map(int, input().split()))
cur_val = sum(nList)
ans = 0

for i in range(N):
    ans += nList[i] * (cur_val - nList[i])
    cur_val -= nList[i]

print(ans)
