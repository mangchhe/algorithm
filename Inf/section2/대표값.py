import sys

#sys.stdin = open('input.txt', 'rt')

n = int(input())

data = list(map(int, input().split()))

# avg = round(sum(data) / n)

# minVal = min(map(lambda x : abs(avg - x), data))

# data2 = []

# for i in range(n):
#     if abs(data[i] - avg) == minVal:
#         data2.append((i, data[i]))

# result = sorted(data2, key=lambda x : -x[1])[0]

# print(avg, result[0] + 1)

avg = int(sum(data) / n + .5)

minVal = float('inf')
score = 0
idx = 0

for i, d in enumerate(data):

    tmp = abs(d - avg)

    if tmp < minVal:
        score = d
        minVal = tmp
        idx = i
    elif tmp == minVal:
        if score < d:
            score = d
            idx = i

print(avg, idx + 1)

