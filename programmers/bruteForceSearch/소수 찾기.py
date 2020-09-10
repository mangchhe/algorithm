""" 
    작성일 : 20/09/10
"""

import itertools

def solution(numbers):

    count = 0

    tmp = list(itertools.permutations(numbers))
    tmp = [i[0] if len(i) == 1 else i for i in tmp]
    tmp.extend(numbers)

    for i in set(map(lambda x: int(''.join(x)), tmp)):
        for j in range(2, i+1):
            if j == i:
                count +=1
            elif i % j == 0:
                break

    return count

print(solution('17'))