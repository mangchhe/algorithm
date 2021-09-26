# https://www.acmicpc.net/problem/1654

input = __import__('sys').stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

l, r = 1, max(lans)

while l <= r:
    mid = (l + r) // 2
    lanCnt = 0
    for lan in lans:
        lanCnt += lan // mid
    if lanCnt >= N:
        l = mid + 1
    else:
        r = mid - 1

print(l - 1)
