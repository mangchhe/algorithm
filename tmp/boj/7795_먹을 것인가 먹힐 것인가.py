T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    AList = list(map(int, input().split()))
    BList = list(map(int, input().split()))
    AList.sort()
    BList.sort()
    ans = 0

    r = 0 
    for i in range(A):
        while r < B and AList[i] > BList[r]:
            r += 1
        ans += r

    print(ans)
