''' 시간 초
from sys import stdin

def solve(start, end, i, val):

    mid = (start + end) // 2

    if NList[mid] == val:

        CList.append(1)

        isList[mid] = False

        solve2(mid, i, val)

    elif start == end:

        CList.append(0)

    elif NList[mid] < val:

        solve(mid + 1, end, i, val)

    elif NList[mid] > val:

        solve(start, mid, i, val)

def solve2(idx, i, val):

    if idx + 1 < N and isList[idx + 1] and NList[idx + 1] == val:

        CList[i] += 1

        isList[idx + 1] = False

        solve2(idx + 1, i, val)

    if idx - 1 > -1 and isList[idx - 1] and NList[idx - 1] == val:

        CList[i] += 1

        isList[idx - 1] = False

        solve2(idx - 1, i, val)

if __name__ == '__main__':

    N = int(stdin.readline())

    NList = list(map(int, stdin.readline().split()))

    M = int(stdin.readline())

    MList = list(map(int, stdin.readline().split()))

    CList = []

    NList.sort()

    for i, j in enumerate(MList):

        isList = [True for i in range(N)]

        solve(0, N - 1, i, j)

    for i in CList:

        print(i, end=' ')
'''

# Lower bound
# Upper bound

from sys import stdin

def lowerBound(start, end, val):

    while start < end:

        mid = (start + end) // 2

        if NList[mid] < val:

            start = mid + 1

        else:

            end = mid

    return end

def upperBound(start, end, val):

    while start < end:

        mid = (start + end) // 2

        if NList[mid] <= val:

            start = mid + 1

        else:

            end = mid

    return end


if __name__ == '__main__':

    N = int(stdin.readline())

    NList = list(map(int, stdin.readline().split()))

    M = int(stdin.readline())

    MList = list(map(int, stdin.readline().split()))

    NList.sort()

    print(NList)

    for i in MList:

        s = lowerBound(0, N - 1, i)
        e = upperBound(0, N - 1, i)

        print(s, e, e-s, end=' ')
        print()
