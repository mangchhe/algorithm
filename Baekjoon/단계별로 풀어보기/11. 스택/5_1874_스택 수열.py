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

for i in range(int(input())):

    N = int(sys.stdin.readline().strip())

    if last <= N:
        for j in range(last, N+1):
            print('+')
            stack.append(i)

            if j == N:
                print('-')
                last = j
                del stack[-1]
    else:
        for j in range(last, N-1, -1):
            print('-')
            del stack[-1]