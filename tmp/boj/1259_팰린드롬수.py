input = __import__('sys').stdin.readline

while True:
    N = input().rstrip()
    if N == '0':
        break
    length = len(N)
    ans = 'no'
    if length % 2 == 0:
        if N[:length // 2] == N[length // 2:][::-1]:
            ans = 'yes'
    else:
        if N[:length // 2] == N[length // 2 + 1:][::-1]:
            ans = 'yes'

    print(ans)
