input = __import__('sys').stdin.readline

def insert(val):
    global res
    res -= cnt[val] ** 2 * val
    cnt[val] += 1
    res += cnt[val] ** 2 * val

def delete(val):
    global res
    res -= cnt[val] ** 2 * val
    cnt[val] -= 1
    res += cnt[val] ** 2 * val

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
    N, T = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    query = []
    cnt = [0] * 1000001
    ans = [0] * T
    res = 0
    for i in range(T):
        s, e = map(int, input().split())
        query.append((s, e, i))

    query.sort(key=lambda x: (int(x[0] ** .5), x[1]))

    l = r = query[0][0]
    r -= 1
    
    for i in range(T):
        s, e, idx = query[i]
        move(l, r, s, e)
        l, r = s, e
        ans[idx] = res

    for i in ans:
        print(i)
