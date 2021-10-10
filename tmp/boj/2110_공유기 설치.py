# https://www.acmicpc.net/problem/2110

input = __import__('sys').stdin.readline

N, C = map(int, input().split())
distance = [int(input()) for _ in range(N)]
distance.sort()
ans = 0

l, r = 1, distance[-1] - distance[0]

while l <= r:
    mid = (l + r) // 2
    cnt = 1
    now = 0
    
    for i in range(1, len(distance)):
        if distance[now] + mid <= distance[i]:
            cnt += 1
            now = i

    if cnt >= C:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
