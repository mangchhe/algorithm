import sys

# sys.stdin = open('input.txt', 'rt')

resArr = []

def dfs(v):

    if v > n:
        return
    else:
        resArr.append(v)
        dfs(v + 1)
        print(' '.join(map(str, resArr)))
        resArr.pop()
        dfs(v + 1)


if __name__ == '__main__':

    n = int(input())

    dfs(1)