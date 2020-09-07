""" 
    작성일 : 20/09/07 - 진행중
"""

import heapq

def solution(jobs):

    jobs = list(map(lambda x: [x[1], x[0]], jobs))

    start = 1
    end = 0
    current = 0 + jobs[0][0]
    result = 0 + jobs[0][0]
    
    while True:
        for i in range(start, len(jobs)):
            if current < jobs[i][1]:
                end = i - 1
            elif current == jobs[i][1]:
                end = i
            elif i == len(jobs) - 1:
                end = i
        tmp = jobs[start:end+1]
        start = end + 1
        heapq.heapify(tmp)

        for i in range(len(tmp)):
            tmp2 = heapq.heappop(tmp)
            result += current - tmp2[1] + tmp2[0]
            current += tmp2[0]

        if end == len(jobs) - 1:
            break

    return result // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6], [4, 3]]))