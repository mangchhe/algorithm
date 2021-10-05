# https://www.acmicpc.net/problem/10808

wordCnt = [0] * 26

for i in input():
    wordCnt[ord(i) - 97] += 1

for i in wordCnt:
    print(i, end=" ")
