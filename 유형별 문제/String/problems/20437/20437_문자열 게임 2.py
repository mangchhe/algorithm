from collections import defaultdict

input = __import__("sys").stdin.readline

for _ in range(int(input())):
    recodes = defaultdict(list)
    data = input().rstrip()
    for i, s in enumerate(data):
        recodes[s].append(i)
    K = int(input())
    minVal = float("INF")
    maxVal = 0
    for r in recodes:
        if len(recodes[r]) < K:
            continue
        for i in range(len(recodes[r]) - K + 1):
            length = recodes[r][i + K - 1] - recodes[r][i]
            minVal = min(minVal, length)
            maxVal = max(maxVal, length)
    if K == 1:
        print("1 1")
    elif maxVal:
        print(minVal + 1, maxVal + 1)
    else:
        print(-1)
