N = int(input())
words = []
wordDic = {}

for _ in range(N):
    word = input()
    words.append(word)
    cnt = 0
    for i in range(len(word)-1, -1, -1):
        wordDic[word[i]] = wordDic.get(word[i], 0) + 1 * (10 ** cnt)
        cnt += 1

n = 9
for i in sorted(wordDic.items(), key=lambda x: -x[1]):
    for j in range(len(words)):
        words[j] = words[j].replace(i[0], str(n))
    n -= 1

print(sum(map(int, words)))
