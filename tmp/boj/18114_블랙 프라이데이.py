N, C = map(int, input().split())
numDic = {}
nums = sorted(map(int, input().split()))
for num in nums:
    if not numDic.get(num):
        numDic[num] = 1

if numDic.get(C):
    print(1)
    exit()

for i in range(N):
    for j in range(i + 1, N):
        total = nums[i] + nums[j]
        if C - total > nums[-1]:
            break
        if total == C:
            print(1)
            exit()
        if numDic.get(C - total) and nums[i] != C - total and nums[j] != C - total:
            print(1)
            exit()

print(0)
