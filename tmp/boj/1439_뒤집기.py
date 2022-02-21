S = list(map(int, list(input())))
prev = ''
changeCnt = 0

for s in S:
    if prev != s:
        changeCnt += 1
        prev = s

print(changeCnt // 2)
