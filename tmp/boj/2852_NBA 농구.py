# https://www.acmicpc.net/problem/2852

memo = []

for _ in range(int(input())):
    t, time = input().split()
    m, s = map(int, time.split(":"))
    memo.append((int(t) - 1, m * 60 + s))

beforeTime = memo[0][1]
teamPoint = [0] * 2
ans = [0] * 2
teamPoint[memo[0][0]] += 1

for i in range(1, len(memo)):
    if teamPoint[0] > teamPoint[1]:
        ans[0] += memo[i][1] - beforeTime
    elif teamPoint[0] < teamPoint[1]:
        ans[1] += memo[i][1] - beforeTime

    beforeTime = memo[i][1]
    teamPoint[memo[i][0]] += 1
else:
    if teamPoint[0] > teamPoint[1]:
        ans[0] += 2880 - beforeTime
    elif teamPoint[0] < teamPoint[1]:
        ans[1] += 2880 - beforeTime

s, r = map(str, divmod(ans[0], 60))
print(''.join(['0' * (2 - len(s)) + s, ":", '0' * (2 - len(r)) + r]))
s, r = map(str, divmod(ans[1], 60))
print(''.join(['0' * (2 - len(s)) + s, ":", '0' * (2 - len(r)) + r]))
