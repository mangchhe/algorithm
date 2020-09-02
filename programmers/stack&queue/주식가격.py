""" 
    작성일 : 20/09/02 - 완료
"""

def solution(prices):

    length = len(prices)
    result = []

    for i in range(length):
        for j in range(i, length):
            if prices[i] > prices[j]:
                result.append(j-i)
                break
            if j == length - 1:
                result.append(length - i - 1)

    return result
            
print(solution([1, 2, 3, 2, 3]))