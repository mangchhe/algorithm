"""
cnt = 숫자 빈도 수
table = 숫자 빈도수 카운터
res = 현재 가장 빈도수
"""

input = __import__('sys').stdin.readline

def init():
    _, _, idx = pQuery[0]
    s, e = query[idx]
    for i in range(s, e + 1):
        insert(arr[i])
    ans[idx] = res

def insert(idx):
    global res
    if cnt[idx] != 0:
        table[cnt[idx]] -= 1
    cnt[idx] += 1
    table[cnt[idx]] += 1
    res = max(res, cnt[idx])

def delete(idx):
    global res
    table[cnt[idx]] -= 1
    if cnt[idx] == res and not table[cnt[idx]]:
        res -= 1
    cnt[idx] -= 1
    table[cnt[idx]] += 1

def move(ss, se, es, ee):
    for i in range(ss, es):
        delete(arr[i])
    for i in range(se, ee, -1):
        delete(arr[i])
    for i in range(ss - 1, es - 1, -1):
        insert(arr[i])
    for i in range(se + 1, ee + 1):
        insert(arr[i])

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    query = []
    pQuery = []
    cnt = [0] * 100001
    table = [0] * 100001
    res = 0
    ans = [0] * 100001
    for i in range(M):
        s, e = map(int, input().split())
        s, e = s - 1, e - 1
        query.append((s, e))
        pQuery.append((int(s ** .5), e, i))

    pQuery.sort()

    init()

    for i in range(1, M):
        ss, se = query[pQuery[i - 1][2]]
        es, ee = query[pQuery[i][2]]
        move(ss, se, es, ee)
        ans[pQuery[i][2]] = res

    for i in range(M):
        print(ans[i])
