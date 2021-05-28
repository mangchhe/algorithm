n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x: x[2])

parent = [i for i in range(n + 1)]
cnt = 0
dis = 0

def getParent(parent, x):

    if parent[x] == x:
        return parent[x]
    
    parent[x] = getParent(parent, parent[x])

    return parent[x]

def unionParent(parent, x, y):

    x = getParent(parent, x)
    y = getParent(parent, y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def find(parent, x, y):

    if getParent(parent, x) == getParent(parent, y):
        return True
    
    return False

for x, y, c in arr:

    if find(parent, x, y):
        continue
    else:
        cnt += 1
        dis += c
        unionParent(parent, x, y)
        if cnt == n - 2:
            print(dis)
            break