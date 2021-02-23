import sys

# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())

cnt = [0] * (n + m + 2)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

maxVal = max(cnt)

for idx, val in enumerate(cnt):
    if maxVal == val:
        print(idx, end=' ')


# from collections import Counter

# tmp = []
# for i in range(1, n + 1):
#     for j in range(1, m + 1): 
#         tmp.append(i + j)

# print(Counter(tmp).most_common(3))