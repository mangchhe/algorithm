'''
※ 입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다.
둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

※ 출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다.
push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
'''

import sys

stack = []
last = 1
result = []

for i in range(int(input())):

    N = int(sys.stdin.readline().strip())

    if N >= last:
        for i in range(last, N+1):
            stack.append(i)
            result.append('+')
        last = stack[-1] + 1
        del stack[-1]
        result.append('-')
    else:
        try:
            for i in range(len(stack) - stack.index(N)):
                del stack[-1]
                result.append('-')
        except:
            del result
            break

try:
    for i in result:
        print(i)
except:
    print('NO')

# 동국대 NAVER

from sys import stdin
from collections import deque
'''
deque 는 스택과 큐의 기능을 모두 가진 객체
※ 메서드 종류
1. append()
2. appendleft()
3. pop()
4. popleft()
5. extend()
6. extendleft()
7. insert()
8. remove()
9. reverse()
'''
a = list(map(int, stdin.read().split()))[1:]
'''
sys.stdin.readline : 띄어쓰기와 \n까지 포함
sys.stdin : 여러줄 입력 (^Z 시 종료)
'''
r = 1
q = deque()
res = []
for x in a:
    while x >= r:
        q.append(r)
        res.append('+')
        r += 1
    if q[-1] == x:
        res.append('-')
        q.pop()
    else:
        print('NO')
        exit()
print('\n'.join(res))
'''
split 문자열 -> 리스트
join 리스트 -> 문자열
'''