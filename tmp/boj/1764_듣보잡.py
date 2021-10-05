# https://www.acmicpc.net/problem/1764

input = __import__('sys').stdin.readline

# 방법 1
# Dictionary 자료구조 이용

from collections import defaultdict

N, M = map(int, input().split())
humans = defaultdict(int)

for i in range(N):
    humans[input().rstrip()] += 1

for i in range(M):
    humans[input().rstrip()] += 1

ans = sorted(filter(lambda x: humans[x] > 1, humans))

print(len(ans))

for i in ans:
    print(i)

# 방법 2
# Set 자료구조 이용

N, M = map(int, input().split())
noListen = set()
noSee = set()

for _ in range(N):
    noListen.add(input().rstrip())

for _ in range(M):
    noSee.add(input().rstrip())

ans = sorted(noListen & noSee)

print(len(ans))

for i in ans:
    print(i)
