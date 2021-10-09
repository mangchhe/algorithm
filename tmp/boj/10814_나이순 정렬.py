# https://www.acmicpc.net/problem/10814

from collections import defaultdict

input = __import__('sys').stdin.readline

N = int(input())
users = [input().split() for _ in range(N)]

userDic = defaultdict(list)

for user in users:
    userDic[int(user[0])].append(user[1])

for i in sorted(userDic.keys()):
    for j in userDic[i]:
        print(i, j)
