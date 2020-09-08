""" 
    작성일 : 20/09/08 - 진행중
"""

from itertools import permutations
import heapq

""" def solution(numbers):

    return max(map(lambda x: ''.join(x), permutations(map(str, numbers)))) """

""" def solution(numbers):

    numbers = list(map(str, numbers))
    heapq.heapify(numbers)
    result = ''
    while numbers:
        result = heapq.heappop(numbers)+ result

    return result """



print(solution([6, 10, 2, 1]))