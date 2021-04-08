def solution(s):
    s = list(s)
    sLen = len(s)
    res = float('INF')

    for i in range(1, sLen + 1):
        n = sLen // i
        cnt = 1
        tmp = s[0:i]
        ccnt = sLen % i
        for j in range(1, n + 1):
            if s[0 + i * j:i + i * j] == tmp:
                cnt += 1
            else:
                tmp = s[0 + i * j:i + i * j]
                if cnt == 1:
                    ccnt += i
                else:
                    ccnt += i + len(str(cnt))
                    cnt = 1

        if res > ccnt:
            res = ccnt

    return res