import sys
import heapq
input = sys.stdin.readline

def mst(start):
    global lanTotal
    h = graph[start]
    heapq.heapify(h)
    visited[start] = 1
    cnt = 1

    while h:
        c, s, e = heapq.heappop(h)
        if visited[e]:
            continue
        visited[e] = 1
        lanTotal -= c
        cnt += 1
        if cnt == N:
            break
        for node in graph[e]:
            if not visited[node[2]]:
                heapq.heappush(h, node)
    else:
        return False

    return True

def chrToLength(s):
    ret = 0
    if s == '0':
        ret = 0
    elif s.islower():
        ret = ord(s) - 96
    else:
        ret = ord(s) - 38
    
    return ret

N = int(input())
lans = [list(map(chrToLength, list(input().rstrip()))) for _ in range(N) ]
graph = [[] for _ in range(N)]
visited = [0] * N
lanTotal = sum(map(sum, lans))
usedLanTotal = 0

for i in range(N):
    for j in range(1 + i, N):
        c = 0
        if lans[i][j] == 0 and lans[j][i] == 0:
            continue
        elif lans[i][j] == 0 or lans[j][i] == 0:
            c = max(lans[i][j], lans[j][i])
        else:
            c = min(lans[i][j], lans[j][i])
        
        graph[i].append([c, i, j])
        graph[j].append([c, j, i])


if mst(0) or N == 1:
    print(lanTotal - usedLanTotal)
else:
    print(-1)
