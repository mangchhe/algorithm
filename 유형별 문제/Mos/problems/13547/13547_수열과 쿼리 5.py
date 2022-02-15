input = __import__('sys').stdin.readline

def init():
    global otherCnt
    for i in range(query[priorityQuery[0][2]][0], query[priorityQuery[0][2]][1] + 1):
        if cnt[arr[i]] == 0:
            otherCnt += 1
        cnt[arr[i]] += 1
    ans[priorityQuery[0][2]] = otherCnt

def insert(idx):
    global otherCnt
    val = arr[idx]
    if cnt[val] == 0:
        otherCnt += 1
    cnt[val] += 1

def delete(idx):
    global otherCnt
    val = arr[idx]
    if cnt[val] == 1:
        otherCnt -= 1
    cnt[val] -= 1

def getDifferenceCnt(ss, se, es, ee):
    for i in range(ss, es):
        delete(i)
    for i in range(ss - 1, es - 1, -1):
        insert(i)
    for i in range(se + 1, ee + 1):
        insert(i)
    for i in range(se, ee, -1):
        delete(i)

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    query = []
    priorityQuery = []
    otherCnt = 0
    cnt = [0] * 1000001
    ans = [0] * M
    for i in range(M):
        s, e = map(int, input().split())
        s, e = s - 1, e - 1
        query.append([s, e])
        priorityQuery.append([s // (N // int(N ** .5)), e, i])
    
    priorityQuery.sort()
    init()
    
    for i in range(1, len(priorityQuery)):
        getDifferenceCnt(query[priorityQuery[i - 1][2]][0], query[priorityQuery[i - 1][2]][1], query[priorityQuery[i][2]][0], query[priorityQuery[i][2]][1])
        ans[priorityQuery[i][2]] = otherCnt

    for i in ans:
        print(i)
