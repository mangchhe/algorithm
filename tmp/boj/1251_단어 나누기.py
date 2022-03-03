def solve(words):
    global ans
    w = ''.join(list(map(lambda x: x[::-1], words)))
    if ans > w:
        ans = w

def traverse(now, n, cnt, words):
    if cnt == 2:
        words.append(s[now:])
        solve(words)
        words.pop()
    else:
        for i in range(1, length - n):
            words.append(s[now:now + i])
            traverse(now + i, n + i, cnt + 1, words)
            words.pop()


s = input()
length = len(s)
ans = 'z' *  50

traverse(0, 0, 0, [])

print(ans)
