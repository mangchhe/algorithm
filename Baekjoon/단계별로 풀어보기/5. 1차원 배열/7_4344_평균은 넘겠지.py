C = int(input())

for i in range(C):
    # sum = 0
    avg = 0
    count = 0

    N = list(map(int, input().split()))

    # 1. 알고리즘

    #for j in range(1,len(N)):
    #    sum += N[j]
    #    avg = sum / N[0]

    # 2. 기존 라이브러리, 슬라이싱

    avg = sum(N[1:]) / N[0]

    for j in range(1,len(N)):
        if avg < N[j]:
            count += 1

    print('%.3f' % (count / N[0] * 100), end='%\n')
