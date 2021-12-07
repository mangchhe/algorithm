from collections import defaultdict

# 방법1
for _ in range(int(input())):
    textCnt = defaultdict(int)
    for s in input():
        if s != ' ':
            textCnt[s] += 1
    maxVal = max(textCnt.values())
    tmp = list(filter(lambda x: x[1] == maxVal, textCnt.items()))
    if len(tmp) == 1:
        for i in tmp: print(i[0])
    else:
       print('?')

# 방법 2
for _ in range(int(input())):
    cnts = [0] * 26
    for s in input().replace(" ", ""):
        cnts[ord(s) - 97] += 1
    maxVal = max(cnts)
    if cnts.count(maxVal) > 1:
        print('?')
    else:
        print(chr(cnts.index(maxVal) + 97))
