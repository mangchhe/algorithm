ans = []
score = 0

def traverse(arrow, cnt, ryan, apeach):
    global score, ans
    if cnt > 10 or arrow == 0:
        if arrow - 1:
            ryan[0] += arrow - 1
        ryanScore = 0
        apeachScore = 0
        for i in range(11):
            if ryan[i] == 0 and apeach[i] == 0:
                continue
            if ryan[i] > apeach[i]:
                ryanScore += i
            else:
                apeachScore += i
        if ryanScore > apeachScore and ryanScore - apeachScore >= score:
            ans = ryan[:]
            score = ryanScore - apeachScore
        if arrow - 1:
            ryan[0] -= arrow - 1
        return
                
    for i in range(arrow):
        ryan[cnt] = i
        traverse(arrow - i, cnt + 1, ryan, apeach)
        ryan[cnt] = 0

def solution(n, info):
    traverse(n + 1, 0, [0] * 11, info[::-1])
    if not ans:
        return [-1]
    return ans[::-1]
