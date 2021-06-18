from sys import stdin

input = stdin.readline

def findParent(parent, a):

    if parent[a] == a:
        return parent[a]
    
    parent[a] = findParent(parent, parent[a])

    return parent[a]

def unionParent(parent, a, b):

    a = findParent(parent, a)
    b = findParent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def findCycle(parent, a, b):

    if findParent(parent, a) == findParent(parent, b):
        return True
    
    return False

if __name__ == '__main__':

    while True:

        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        parent = [i for i in range(n + 1)]
        cost = 0
        cnt = 0
        distance = []

        for _ in range(m):
            tmp = list(map(int, input().split()))
            cost += tmp[2]
            distance.append(tmp)

        distance.sort(key=lambda x:x[2])

        for a, b, c, in distance:

            if findCycle(parent, a, b):
                continue
            else:
                cnt += 1
                cost -= c

                if cnt == n - 1:
                    print(cost)
                    break

                unionParent(parent, a, b)
