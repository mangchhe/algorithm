""" 
    작성일 : 20/09/01 - 진행중
"""

import collections
from functools import reduce

def solution(clothes):

    answer = list(collections.Counter(list(zip(*clothes))[1]).values())
    length = len(answer)
    start = 0
    end = 1
    ori_end = 1
    result = 0

    while end - start != length:

        result += reduce(lambda x, y : x * y, answer[start:end+1])

        start += 1
        end += 1

        if length - 1 < end:
            start = 0
            ori_end += 1
            end = ori_end

    return result + sum(answer)

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
