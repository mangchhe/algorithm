input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N = int(input())
    s1 = list(input().rstrip())
    s2 = list(input().rstrip())
    bCnt = 0
    wCnt = 0
    ans = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        if s1[i] == 'B':
            bCnt += 1
        else:
            wCnt += 1

        tmp = sorted([bCnt, wCnt])
        tmp[1] -= tmp[0]
        ans = tmp[0]

        if tmp[1]:
            ans += tmp[1]

    print(ans)
