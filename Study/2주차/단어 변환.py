cnt, res = 0, float('INF')


def compareWords(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            cnt += 1
    if cnt == len(s1) - 1:
        return True
    else:
        return False


def dfs(begin, target, words, visited):

    global cnt, res

    if begin == target:
        res = min(res, cnt)
    else:
        for i in range(len(words)):
            if compareWords(begin, words[i]) and visited[i] == 0:
                visited[i] = 1
                cnt += 1
                dfs(words[i], target, words, visited)
                visited[i] = 0
                cnt -= 1


def solution(begin, target, words):

    visited = [0] * len(words)

    dfs(begin, target, words, visited)

    if res == float('INF'):
        return 0
    else:
        return res


if __name__ == '__main__':

    solution("hit", "cog", ["dot", "hot", "cog", "log", "dog", "lot"])

    print(res)