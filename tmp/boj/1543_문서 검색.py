s = input()
target = input()
ans = 0

now = 0
while now + len(target) <= len(s):
    for i in range(len(target)):
        if s[now + i] != target[i]:
            now += 1
            break
    else:
        now += len(target)
        ans += 1

print(ans)
