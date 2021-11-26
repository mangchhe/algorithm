input = __import__('sys').stdin.readline

N = int(input())
papers = [0] * 366
ans = 0

for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        papers[i] += 1

term, h = 0, 0
for i in range(1, 366):
    if papers[i] == 0 and term == 0:
        continue
    elif papers[i] == 0:
        ans += term * h
        term, h = 0, 0
    else:
        term += 1
        h = max(h, papers[i])
else:
    ans += term * h

print(ans)
