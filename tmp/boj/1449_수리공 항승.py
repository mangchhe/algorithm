N, L = map(int, input().split())
tapes = list(map(int, input().split()))
tapes.sort()
ans = 1

prev = tapes[0]
for tape in tapes:
    if tape - prev + 1 > L:
        prev = tape
        ans += 1

print(ans)
