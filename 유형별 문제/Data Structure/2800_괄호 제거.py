from itertools import combinations
from functools import reduce

input = __import__("sys").stdin.readline

stack = []
pos = []
cases = []
ans = set()

s = list(input().rstrip())

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    elif s[i] == ")":
        pos.append((stack.pop(), i))

for i in range(1, len(pos) + 1):
    cases.extend(combinations(pos, i))

for case in cases:
    tmp = list(s)
    for erase in reduce(lambda x, y: x + y, case):
        tmp[erase] = ""
    ans.add("".join(tmp))

for res in sorted(ans):
    print(res)
