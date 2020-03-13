# R 배열 숫자 뒤집기 D 첫 번째 숫자를 버리는 함수
# len() - 문자열의 처음부터 끝까지 null이 나올때까지 한 글자씩 확인하므로 O(n) 연산
# reverse - 마찬가지 O(n)

from collections import deque
from sys import stdin

for i in range(int(input())):

    cls = list(stdin.readline())
    stdin.readline()
    try:
        tmp = deque(list(map(int,stdin.readline().strip('[]\n').split(','))))
    except:
        print('error')
        continue

    for val in cls:
        if len(tmp) == 0:
            break
        elif val == 'R':
            tmp.reverse()
        elif val == 'D':
            tmp.popleft()

    if len(tmp):
        print(list(tmp))
    else:
        print('error')