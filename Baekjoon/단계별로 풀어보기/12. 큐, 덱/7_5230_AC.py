# R 배열 숫자 뒤집기 D 첫 번째 숫자를 버리는 함수
# len() - 문자열의 처음부터 끝까지 null이 나올때까지 한 글자씩 확인하므로 O(n) 연산
# reverse - 마찬가지 O(n)

from collections import deque
from sys import stdin

''' 시간초과

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

'''

for i in range(int(input())): # 틀림(반례 찾는중)

    cls = list(stdin.readline())
    stdin.readline()
    rvs = 0
    err_code = False
    try:
        tmp = deque(list(stdin.readline().strip('[]\n').split(',')))
        if tmp[0] == '':
            raise IndexError
    except:
        err_code = True

    for val in cls:
        if val == 'R':
           rvs += 1
        elif val == 'D':
            try:
                if rvs % 2 == 0:
                    tmp.popleft()
                else:
                    tmp.pop()
            except:
                err_code = True
                break
    if err_code:
        print('error')
        continue

    if rvs % 2 == 0:
        pass
    else:
        tmp.reverse()

    print('[',end='')
    for i in range(len(tmp)):
        if(i==len(tmp)-1):
            print(tmp[i],end='')
        else:
            print(tmp[i]+',',end='')
    print(']')