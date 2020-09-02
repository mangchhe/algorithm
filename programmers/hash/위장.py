""" 
    작성일 : 20/09/01 - 진행중
    수정일 : 20/09/02 - 완료
"""

import collections
from functools import reduce

""" def solution(clothes):

    answer = list(collections.Counter(list(zip(*clothes))[1]).values())
    print(answer)
    length = len(answer)
    result = 0

    for i in range(length-1):
        for j in range(i+1, length):
            if abs(i-j) != 1:
                result += reduce(lambda x, y : x * y, answer[i:j+1])
            result += answer[i] * answer[j]

    return result + sum(answer) """

def solution(clothes):

    return reduce(lambda x, y: x * y, map(lambda x : x + 1, collections.Counter(list(zip(*clothes))[1]).values())) - 1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear'], ['green_turba', 'headgear'], ['green_turasdn', 'headgea']]))
