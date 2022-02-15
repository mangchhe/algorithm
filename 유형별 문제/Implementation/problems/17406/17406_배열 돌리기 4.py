from itertools import permutations
import copy

input = __import__("sys").stdin.readline

def rotate(lx, ly, rx, ry):
    lx, ly, rx, ry = lx - 1, ly - 1, rx - 1, ry - 1
    while rx - lx != 0 and ry - ly != 0:
        tmp = [copy_arr[lx][ry], copy_arr[rx][ry], copy_arr[rx][ly]]
        for i in range(ry, ly, -1):
            copy_arr[lx][i] = copy_arr[lx][i - 1]
        for i in range(rx, lx, -1):
            if i == lx + 1: copy_arr[i][ry] = tmp[0]
            else: copy_arr[i][ry] = copy_arr[i - 1][ry]
        for i in range(ly, ry):
            if i == ry - 1: copy_arr[rx][i] = tmp[1]
            else: copy_arr[rx][i] = copy_arr[rx][i + 1]
        for i in range(lx, rx):
            if i == rx - 1: copy_arr[i][ly] = tmp[2]
            else: copy_arr[i][ly] = copy_arr[i + 1][ly]

        lx, ly, rx, ry = lx + 1, ly + 1, rx - 1, ry - 1
        


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
data = [tuple(map(int, input().split())) for _ in range(K)]
copy_arr = []
res = float('INF')
for i in permutations(data, K):
    copy_arr = copy.deepcopy(arr)
    for j in i:
        r, c, s = j
        rotate(r - s, c - s, r + s, c + s)
    for i in copy_arr:
        res = min(res, sum(i))

print(res)