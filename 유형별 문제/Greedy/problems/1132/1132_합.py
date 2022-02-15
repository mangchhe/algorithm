# input = __import__("sys").stdin.readline

# from collections import Counter
# from functools import reduce
# from itertools import permutations

# N = int(input())
# words = [list(input().rstrip()) for _ in range(N)]
# existWords = list(map(lambda x: x[0], Counter(reduce(lambda x, y: x + y, words))))
# numList = permutations(
#     map(str, [i for i in range(9, 9 - len(existWords), -1)]), len(existWords)
# )
# ans = 0

# for num in numList:
#     dic = {}
#     total = 0
#     for existWord, n in zip(existWords, num):
#         dic[existWord] = n
#     for word in words:
#         s = ""
#         for w in word:
#             s += dic[w]
#         total += int(s)

#     ans = max(ans, total)

# print(ans)

from collections import defaultdict

input = __import__("sys").stdin.readline
N = int(input())
words = [list(input().rstrip()) for _ in range(N)]
weight = defaultdict(int)
zeros = []
ans = 0

for word in words:
    for i in range(len(word)):
        if i == 0:
            zeros.append(word[i])
        weight[word[i]] += 10 ** (len(word) - i - 1)

if len(weight) != 10:
    zeros = []

tmp = []

while weight:
    w = weight.popitem()
    tmp.append([w[0], w[1]])

tmp.sort(reverse=True, key=lambda x: x[1])

for i in range(len(tmp) - 1, -1, -1):
    if tmp[i][0] not in zeros:
        tmp.append(tmp[i])
        del tmp[i]
        break

for i in range(len(tmp)):
    ans += tmp[i][1] * (9 - i)

print(ans)
