input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N = int(input())
    l, r = 1, N
    
    res = 0
    while l <= r:
        mid = (l + r) // 2
        if N - (mid * (1 + mid) // 2) >= mid + 1:
            res = max(res, mid)
            l = mid + 1
        else:
            r = mid - 1

    if res == N - (res * (1 + res) // 2):
        print(res)
    else:
        print(res + 1)
