'''
※ 입력
하나 또는 여러줄에 걸쳐서 문자열이 주어진다.
각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

※ 출력
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
'''

import sys

msg = []

while True:

    tmp = list(sys.stdin.readline().rstrip())
    if len(tmp) == 1 and tmp[0] == '.':
        break
    msg.append(tmp)

for i in range(len(msg)):
    stack = []
    flag = True
    for j in msg[i]:
        if j == '(':
            stack.append('(')
        elif j == '[':
            stack.append('[')
        elif j == ']':
            try:
                if stack[-1] == '[':
                    del stack[-1]
                else:
                    flag = False
                    break
            except IndexError:
                flag = False
                break
        elif j == ')':
            try:
                if stack[-1] == '(':
                    del stack[-1]
                else:
                    flag = False
                    break
            except IndexError:
                flag = False
                break
    if flag and len(stack) == 0:
        print('yes')
    else:
        print('no')