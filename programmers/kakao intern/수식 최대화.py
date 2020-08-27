""" 작성일 : 20/08/26 - 진행중
    수정일 : 20/08/27 - 완료
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

            tmpList.append(tmpStr)
            tmpList.append(i)
            tmpStr = ''

        else:

            tmpStr += i

    tmpList.append(tmpStr)

    for i in a:

        tmpList2 = tmpList.copy()
        length = len(tmpList2)

        for j in i:

            start = 1

            while start < length:

                if tmpList2[start] == j:

                    tmpVal = str(eval(tmpList2[start - 1] + j + tmpList2[start + 1]))
                    for i in range(3):
                        del tmpList2[start - 1]
                    tmpList2.insert(start-1, tmpVal)
                    length -= 2

                else:

                    start += 2

        result.append(abs(int(tmpList2[0])))

    return max(result)

solution("50*6-3*2")