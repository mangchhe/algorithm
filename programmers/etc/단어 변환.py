from collections import defaultdict


def diffOne(s1, s2):

    cnt = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            cnt += 1
    if cnt == len(s1) - 1:
        return True
    return False


def bfs(begin, target, words, visited, res, cnt):

    if begin == target:
        res[0] = min(cnt, res[0])
    else:
        for word in words:
            if word not in visited and diffOne(begin, word):
                visited[word]
                bfs(word, target, words, visited, res, cnt + 1)
                del visited[word]


def solution(begin, target, words):

    res = [float('INF')]
    visited = defaultdict(int)

    bfs(begin, target, words, visited, res, 0)

    if res[0] == float('INF'):
        return 0
    else:
        return res[0]


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
