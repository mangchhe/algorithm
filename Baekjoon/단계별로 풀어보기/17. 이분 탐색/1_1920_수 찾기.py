from sys import stdin

def solve(n, m, val):

    num = (n + m) // 2

    if NList[num] == val:

        return 1

    elif n == m:

        return 0

    elif NList[num] > val:

        return solve(n, num, val)

    elif NList[num] < val:

        return solve(num + 1, m, val)


if __name__ == '__main__':

    N = int(stdin.readline())

    NList = list(map(int, stdin.readline().split()))

    M = int(stdin.readline())

    NSearchVal = list(map(int, stdin.readline().split()))

    NList.sort()

    for i in range(M):

        print(solve(0, N - 1, NSearchVal[i]))
