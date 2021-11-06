contents = input().split()
spaceCnt = int(input())
keyCnt = list(map(int, input().split()))
contents.append(''.join(map(lambda x: x[0].upper(), contents)))

if len(contents) - 2 > spaceCnt:
    print(-1)
    exit()

for content in contents:
    before = ''
    for c in content:
        if before == c:
            continue
        if keyCnt[ord(c.upper()) - 65] < 1:
            print(-1)
            exit()
        before = c
        keyCnt[ord(c.upper()) - 65] -= 1

print(contents[-1])
