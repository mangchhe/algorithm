input = __import__('sys').stdin.readline

tip = []
ans = 0

for i in range(int(input())):
    tip.append(int(input()))

tip.sort(reverse=True)

for i in range(len(tip)):
    n = tip[i] - i
    if n > -1:
        ans += n

print(ans)