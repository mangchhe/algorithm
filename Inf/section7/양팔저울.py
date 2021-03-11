import sys

# sys.stdin = open('input.txt', 'rt')

def dfs(v, sum):

    if v >= k:
        resArr.add(abs(sum))
        return
    else:
        dfs(v + 1, sum + data[v])
        dfs(v + 1, sum - data[v])
        dfs(v + 1, sum)


if __name__ == '__main__':
    
    k = int(input())
    data = list(map(int, input().split()))
    resArr = set()

    dfs(0, 0)

    print(sum(data) - len(resArr) + 1)