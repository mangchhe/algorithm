# ★★★★ 재풀이 희망 ★★★★

from collections import defaultdict, deque
import copy

tmpArr = ['ICN']
res = ['ICN']


def dfs(now, ticketDic, visited, cnt):

    global tmpArr, res

    if len(tmpArr) == cnt:
        if len(res) == 1:
            res = copy.copy(tmpArr)
    else:
        for i in range(-1, -len(ticketDic[now]) - 1, -1):
            if visited[now][ticketDic[now][i]] != 0:
                visited[now][ticketDic[now][i]] -= 1
                tmpArr.append(ticketDic[now][i])
                dfs(ticketDic[now][i], ticketDic, visited, cnt)
                tmpArr.pop()
                visited[now][ticketDic[now][i]] += 1


def solution(tickets):

    ticketDic = defaultdict(list)
    visited = defaultdict(list)
    cnt = 1

    for ticket in tickets:
        ticketDic[ticket[0]].append(ticket[1])
        cnt += 1

    for ticket in ticketDic:
        ticketDic[ticket].sort(reverse=True)
        visited[ticket] = defaultdict(int)

    for ticket in tickets:
        visited[ticket[0]][ticket[1]] += 1

    dfs('ICN', ticketDic, visited, cnt)

    return res


print(
    solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['ICN', 'AAA'], ['AAA', 'ICN'],
              ['AAA', 'ICN']]))
