""" 작성일 : 20/08/28 - 시간 초과
    작성자 : 하주현
    내용 : 보석 쇼핑
    주소 : https://programmers.co.kr/learn/courses/30/lessons/67258
"""

def solution(gems):

    answer = ''

    origin = {i : False for i in set(gems)}

    result = {}

    length = len(gems)

    for i in range(0, length - 1):

        tmpDic = origin.copy()

        for j in range(i, length):

            tmpDic[gems[j]] = True

            if all(tmpDic.values()):
                result[(i, j)] = j - i
                break

    min = 999999

    for i, j in result.items():

        if min > j:

            min = j
            answer = i

    answer = list(answer)

    answer[0] += 1
    answer[1] += 1

    return answer