for _ in range(int(input())):
    input()
    minVal, maxVal = 10**6, -10**6

    for i in list(map(int, input().split())):
        minVal = min(minVal, i)
        maxVal = max(maxVal, i)

    print(minVal, maxVal)
