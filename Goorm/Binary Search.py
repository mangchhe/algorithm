from sys import stdin

count = 0

def solve(start, end, findN):

    global count

    count += 1

    if count == 1:

        stop = end // 2

    if count == end:

        return 'X'

    mid = (start + end) // 2

    if box[mid] == findN:

        return mid + 1

    elif box[mid] < findN:

        return solve(mid, end, findN)

    elif box[mid] > findN:

        return solve(start, mid, findN)


N = int(stdin.readline())

box = list(map(int, stdin.readline().split()))

findN = int(stdin.readline())

print(solve(0, len(box) - 1, findN))
