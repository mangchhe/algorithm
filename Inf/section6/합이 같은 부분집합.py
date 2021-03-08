import sys

# sys.stdin = open('input.txt', 'rt')

res = 0
resArr = set()

def dfs(v):

    global res
    
    if v > n - 1:
        return
    else:
        resArr.add(data[v])
        if sum(resArr) - sum(set(data) - resArr) == 0:
            res += 1
        dfs(v + 1)
        resArr.remove(data[v])
        dfs(v + 1)

if __name__ == '__main__':

    n = int(input())

    data = list(map(int, input().split()))

    dfs(0)

    if res != 0:
        print("YES")
    else:
        print("NO")