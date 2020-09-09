""" 
    작성일 : 20/09/08 - 진행중
    수정일 : 20/09/09 - 진행중
"""

from itertools import permutations
import heapq

""" 20/09/08
    def solution(numbers):

    return max(map(lambda x: ''.join(x), permutations(map(str, numbers)))) """

""" 20/09/08
    def solution(numbers):

    numbers = list(map(str, numbers))
    heapq.heapify(numbers)
    result = ''
    while numbers:
        result = heapq.heappop(numbers)+ result

    return result """

def solution(numbers):

    numbers = list(map(str, numbers))
    resultList = []
    count = 0
    maxVal = 0
    for i in numbers:
        count += 1
        tmp = len(i)
        if tmp > maxVal:
            maxVal = tmp
        resultList.append([i,tmp])
    for i in range(count):
        resultList[i][0] += resultList[i][0][resultList[i][1] - 1] * (maxVal - resultList[i][1])
    resultList = sorted(resultList, reverse=True)
    for i in range(count):
        resultList[i][0] = resultList[i][0][0:resultList[i][1]]
    
    return ''.join(list(zip(*resultList))[0])

print(solution([2,20,200]))