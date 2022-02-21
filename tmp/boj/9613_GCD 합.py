input = __import__('sys').stdin.readline

def uclid(a, b):
    if b == 0:
        return a
    
    return uclid(b, a % b)

for _ in range(int(input())):
    N, *arr = list(map(int, input().split()))
    ans = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            ans += uclid(arr[i], arr[j])

    print(ans)
