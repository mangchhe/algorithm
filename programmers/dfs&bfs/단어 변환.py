""" 
    작성일 : 20/09/15 - 진행중
"""

def solution(begin, target, words):

    length = len(target)
    diffCount = []
    for word in words:
        tmp = []
        for i in range(length):
            if target[i] == word[i]:
                tmp.append(1)
            else:
                tmp.append(0)
        diffCount.append(tmp)

    for i in range(length):

        for j in filter(lambda x : x != -1, [idx if val == i + 1 else -1 for idx, val in enumerate(map(sum, diffCount))]):

            print(i, j)

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))