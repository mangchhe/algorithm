import copy

answerList = []

def isSimilarTxt(src, dst):

    if len(src) != len(dst):
        return False
    else:
        for i in range(len(src)):
            if dst[i] == '*':
                pass
            elif src[i] == dst[i]:
                pass
            else:
                return False
    
    return True

def dfs(ub_id, visited, N, idx, cnt):

    global answer

    if cnt == N:
        if sorted(visited) not in answerList:
            answerList.append(sorted(copy.copy(visited)))
    elif idx >= N:
        return
    else:
        for i in range(len(ub_id[idx])):
            if ub_id[idx][i] not in visited:
                visited.append(ub_id[idx][i])
                dfs(ub_id, visited, N, idx + 1, cnt + 1)
                visited.pop()
            else:
                dfs(ub_id, visited, N, idx + 1, cnt)
    

def solution(user_id, banned_id):

    ub_id = []
    visisted = []
    N = len(banned_id)

    for banned in banned_id:
        tmp = []
        for user in user_id:
            if isSimilarTxt(user, banned):
                tmp.append(user)
        ub_id.append(tmp)

    dfs(ub_id, visisted, N, 0, 0)

    return len(answerList)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))