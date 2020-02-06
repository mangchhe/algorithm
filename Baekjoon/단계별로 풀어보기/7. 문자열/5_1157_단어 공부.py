index = 0
num = 0
dupi = 0
S = list(input().upper())
tmp = list(set(S))

for i in range(len(tmp)):
    if num < S.count(tmp[i]):
        num = S.count(tmp[i])
        count = i
        dupi = 0
    elif num == S.count(tmp[i]):
        dupi = 1

if dupi:
    print('?')
else:
    print(tmp[count])
    