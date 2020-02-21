# 1 2 3 4 5 6 7
# 1 3 6 10 15 21 28
# 1 4 10 20 35 56 84
# 1 5 15 35 70 126 210

# 정답

N = int(input())

for i in range(N):
    k = int(input())
    n = int(input())
    if k == 0:
        print(n)
    else:
        tmp = [val for val in range(1,n+1,1)]
        tmp2 = []
        for j in range(k-1):
            for m in range(n):
                if m == 0:
                    tmp2.append(1)
                else:
                    A = 0
                    for v in range(m+1):
                        A += tmp[v]
                    tmp2.append(A)
            tmp = tmp2[:]
            del tmp2[:]

        print(sum(tmp))

# 다른 해설

for i in range(int(input())):
    m = int(input())
    n = int(input())
    a = [i for i in range(1,n+1)]
    for _ in range(m):
        for j in range(1,n):
            a[j] += a[j-1]
    print(a[-1])