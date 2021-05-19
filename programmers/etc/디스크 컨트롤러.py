import heapq


def solution(jobs):

    jobs = sorted(jobs, key=lambda x: x[0])
    cnt = 0
    endCnt = 0
    end = 0
    res = 0
    heap = []

    while endCnt < len(jobs):
        while cnt < len(jobs) and jobs[cnt][0] <= end:
            heapq.heappush(heap, [jobs[cnt][1], jobs[cnt][0]])
            cnt += 1

        if not heap:
            end = jobs[cnt][0]
        else:
            job = heapq.heappop(heap)
            res += job[0] + end - job[1]
            end += job[0]
            endCnt += 1

    return res // len(jobs)


print(solution([[0, 3], [2, 6], [1, 9]]))