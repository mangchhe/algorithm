N, M = map(int, input().split())
alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ans = [['', i] for i in range(N, M + 1)]

for i in range(N, M + 1):
    tmp = list(map(int, str(i)))
    for t in tmp:
        ans[i - N][0] += alpha[t]

ans.sort(key=lambda x: x[0])
_, ans = zip(*ans)
        
for i in range(0, len(ans) // 10 + 1):
    print(*ans[i * 10 : (i + 1) * 10])
