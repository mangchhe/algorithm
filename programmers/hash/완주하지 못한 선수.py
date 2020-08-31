""" 
    작성일 : 20/08/31
"""

""" def solution(participant, completion):

    answer = {}

    for i in participant:
        if i not in answer:
            answer[i] = 1
        else:
            answer[i] += 1

    for i in completion:
        answer[i] -= 1
        if answer[i] == 0:
            del answer[i]
    
    return list(answer.keys())[0] """

""" 2 """

import collections

def solution(participant, completion):

    return list(collections.Counter(participant) - collections.Counter(completion))[0] 

print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))