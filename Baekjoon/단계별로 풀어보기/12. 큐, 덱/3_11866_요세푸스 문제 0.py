'''
※ 입력
7 3

※ 출력
<3, 6, 2, 7, 5, 1, 4>
'''

from collections import deque

N, K = list(map(int, input().split()))

tmp = deque(val for val in range(1, N + 1))
result = []

while len(tmp):

    for i in range(K - 1):
        tmp.append(tmp.popleft())

    result.append(tmp.popleft())

print('<', end='')

for i in range(len(result)):
    if i != len(result) - 1:
        print(str(result[i])+',', end=' ')
    else:
        print(result[i], end='>')