""" 
    작성일 : 20/09/11
"""

def solution(n, lost, reserve):

    borrowColothes = 0

    tmp = set(lost) & set(reserve)
    lost = list(set(lost) - tmp)
    reserve = list(set(reserve) - tmp)
    reserve.sort()

    for i in sorted(lost):
        for i in filter(lambda x: x == i-1 or x == i+1, filter(lambda x: x<i+2, reserve)):
            del reserve[reserve.index(i)]
            borrowColothes += 1
            break
    
    return n - len(lost) + borrowColothes

print(solution(5, [1,2], [2,3]))