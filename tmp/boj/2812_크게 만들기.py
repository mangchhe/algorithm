n, k = map(int, input().split())
num = list(map(int, list(input())))

s = []

for i in range(n):
    while len(s) > 0 and k > 0 and s[-1] < num[i]:
        s.pop()
        k -= 1

    s.append(num[i])

if k > 0:
    s = s[:-k]

print(''.join(map(str, s)))
