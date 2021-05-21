# 첫번 째 시도
# import sys

# sys.setrecursionlimit(10**6)

# answer = [0, float('INF')]

# def dfs(N, gems, gemSet, s, e):

#     global answer

#     if s >= N:
#         return
#     elif e > N:
#         dfs(N, gems, gemSet, s + 1, e)
#     else:
#         if len(gemSet) == len(set(gems[s:e])):
#             if answer[1] - answer[0] > e - s:
#                 answer = [s + 1, e]
#             dfs(N, gems, gemSet, s + 1, e)
#         else:
#             dfs(N, gems, gemSet, s, e + 1)

# def solution(gems):
#     gemSet = set(gems)
#     N = len(gems)

#     dfs(N, gems, gemSet, 0, 0)

#     return answer

# from collections import defaultdict

# 두 번째 시도
# def solution(gems):

#     gemDic = defaultdict(int)
#     s, e = 0, 0
#     answer = [0, float('INF')]
#     N = len(gems)

#     for gem in set(gems):
#         gemDic[gem]

#     gemDic[gems[0]] += 1

#     while s < N and e < N:
#         if all(gem > 0 for gem in gemDic.values()):
#             if answer[1] - answer[0] > e - s:
#                 answer = [s + 1, e + 1]
#             gemDic[gems[s]] -= 1
#             s += 1
#         else:
#             e += 1
#             if e == N:
#                 continue
#             gemDic[gems[e]] += 1

#     return answer

# 세번 째 시도

from collections import defaultdict


def solution(gems):

    gemDic = defaultdict(int)
    s, e = 0, 0
    answer = [0, float('INF')]
    N = len(gems)
    size = len(set(gems))

    gemDic[gems[0]] += 1

    while s < N and e < N:
        if len(gemDic) == size:
            if answer[1] - answer[0] > e - s:
                answer = [s + 1, e + 1]
            if gemDic[gems[s]] == 1:
                del gemDic[gems[s]]
            else:
                gemDic[gems[s]] -= 1
            s += 1
        else:
            e += 1
            if e == N:
                continue
            gemDic[gems[e]] += 1

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

print(solution(gems))
