input = __import__('sys').stdin.readline

bar = list(input().rstrip())

ans = 0
s = []

for i in range(len(bar)):
    if bar[i] == '(':
        s.append('(')
    else:
        s.pop()
        if bar[i - 1] == '(':
            ans += len(s)
        else:
            ans += 1

print(ans)
