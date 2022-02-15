input = __import__('sys').stdin.readline

def insert(idx):
    nums[idx] += 1

def delete(idx):
    nums[idx] -= 1

def capture(ss, se, es, ee):
    for i in range(ss, es):
        delete(hats[i])
    for i in range(se, ee, -1):
        delete(hats[i])
    for i in range(ss - 1, es - 1, -1):
        insert(hats[i])
    for i in range(se + 1, ee + 1):
        insert(hats[i])

if __name__ == '__main__':
    N, C = map(int, input().split())
    hats = list(map(int, input().split()))
    M = int(input())
    query = []
    nums = [0] * (C + 1)
    ans = [-1] * M

    for i in range(M):
        s, e = map(int, input().split())
        s, e = s - 1, e - 1
        query.append((s, e, i))
    
    query.sort(key = lambda x: (int(x[0] ** .5), x[1]))

    l = r = query[0][0]
    r -= 1

    for i in range(M):
        s, e, idx = query[i]
        capture(l, r, s, e)
        l, r = s, e
        ret = -1
        length = e - s + 1
        for j in range(1, C + 1):
            if nums[j] > length / 2:
                ret = j
        ans[idx] = ret

    for i in range(M):
        if ans[i] == -1:
            print("no")
        else:
            print("yes", ans[i])
