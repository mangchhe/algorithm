""" 작성일 : 20/08/26
    작성자 : 하주현
    내용 : 수식 최대화
    주소 : https://programmers.co.kr/learn/courses/30/lessons/67257
"""

def solution(expression):

    a = [
        ['+', '-', '*'],
        ['-', '+', '*'],
        ['+', '*', '-'],
        ['*', '+', '-'],
        ['-', '*', '+'],
        ['*', '-', '+']
    ]

    tmp = list(expression)
    tmpList = []
    tmpStr = ''
    giho = ['-', '+', '*']
    result = []

    for i in tmp:

        if i in giho:

            tmpList.append(int(tmpStr))
            tmpList.append(i)
            tmpStr = ''

        else:

            tmpStr += i

    tmpList.append(int(tmpStr))

    answer = 0
    return answer

solution("100-2145*458+12")