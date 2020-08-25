""" 작성일 : 20/08/25
    작성자 : 하주현
    내용 : 키패드 누르기
    주소 : https://programmers.co.kr/learn/courses/30/lessons/67256
"""
def solution(numbers, hand):

    answer = ''
    L = '*'
    R = '#'
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            L = i
        elif i in [3, 6, 9]:
            answer += 'R'
            R = i
        else:
            L_pos = 0
            R_pos = 0
            C_pos = 0

            for k in range(4):
                for l in range(3):
                    if keypad[k][l] == L:
                        L_pos = (k, l)
                    if keypad[k][l] == R:
                        R_pos = (k, l)
                    if keypad[k][l] == i:   
                        C_pos = (k, l)

            LL = abs(L_pos[0] - C_pos[0]) + abs(L_pos[1] - C_pos[1])
            RR = abs(R_pos[0] - C_pos[0]) + abs(R_pos[1] - C_pos[1])

            if LL == RR:
                if hand == 'right':
                    answer += 'R'
                    R = i
                elif hand == 'left':
                    answer += 'L'
                    L = i
            elif LL > RR:
                answer += 'R'
                R = i
            else:
                answer += 'L'
                L = i

    return answer