eng = input()
engDic = {}
ans = ''

for e in eng:
    engDic[e] = engDic.get(e, 0) + 1

holEng = ''
for e, cnt in engDic.items():
    if cnt % 2 == 0:
        continue

    if holEng:
        print('I\'m Sorry Hansoo')
        exit()

    holEng = e

if holEng:
    ans = holEng
    engDic[holEng] -= 1

for e, cnt in sorted(engDic.items(), key=lambda x: -ord(x[0])):
    cnt = cnt // 2
    ans = e * cnt + ans + e * cnt

print(ans)
