# https://www.acmicpc.net/problem/1181

input = __import__('sys').stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
wordDic = {}

for word in words:
    if not wordDic.get(len(word)):
        wordDic[len(word)] = {word}
    else:
        wordDic[len(word)].add(word)

for i in sorted(wordDic.keys()):
    for j in sorted(wordDic[i]):
        print(j)
