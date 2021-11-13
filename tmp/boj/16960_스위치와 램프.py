N, M = map(int, input().split())
lamps = {str(i) : 0 for i in range(1, M + 1)}
switchs = []
ans = 0

for _ in range(N):
    s = input().split()
    switchs.append(s[1:])
    for i in s[1:]:
        lamps[i] += 1

for switch in switchs:
    for s in switch:
        if lamps[s] - 1 == 0:
            break
    else:
        ans = 1
        break

print(ans)
