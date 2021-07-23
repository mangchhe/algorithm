input = __import__("sys").stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))

tmp = []
maxVal = 0
ans = 0

for i in block:
    if i >= maxVal:
        ans += sum(map(lambda x: maxVal - x, tmp))
        tmp = []
        maxVal = i
    else:
        tmp.append(i)

while tmp:
    m = max(tmp)
    idx = tmp.index(m)
    ans += sum(map(lambda x: m - x, tmp[:idx]))
    tmp = tmp[idx + 1 :]

print(ans)
