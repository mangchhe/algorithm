""" 
    작성일 : 20/09/03 - 완료
"""

from collections import deque
from math import ceil

""" def solution(progressess, speeds):

    result = []
    progressess = deque(map(lambda x: ceil((100 -x[0]) / x[1]), zip(progressess, speeds)))

    while progressess:
        trash = []
        init = progressess.popleft()
        for i in range(len(progressess)):
            if init >= progressess[i]:
                trash.append(i)
            else:
                break
        trash.reverse()

        for i in trash:
            del progressess[i]
        
        result.append(1 + len(trash))

    return result """

""" 다른 사람 풀이 """

# // -> 소수점은 무조건 낮은 쪽으로 -> math.ceil 이용
# but, -((p-100)//s) 음수의 경우 먼저 나누고 -를 붙여주면 올림 처리 효과를 볼 수 있다.

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
            
    return [q[1] for q in Q]

print(solution( [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))