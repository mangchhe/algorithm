def solution(s):
    s = list(map(lambda x: list(map(lambda x: int(x), x.split(','))), s[2:len(s)-2].split('},{')))
    
    tmp = [0] * len(s)
    for i in s:
        tmp[len(i) - 1] = i
        
    ans = []
    for i in range(len(s)):
        for t in tmp[i]:
            if t not in ans:
                ans.append(t)
                break
    
    return ans
