N = int(input())
words = [input() for _ in range(N)]
patterns = []
ans = 0

for word in words:
    tmp = []
    word_cnt = [0] * 26
    cnt = 1
    for w in word:
        if word_cnt[ord(w) - 97] == 0:
            word_cnt[ord(w) - 97] = cnt
            cnt += 1
        tmp.append(word_cnt[ord(w) - 97])
    patterns.append(tmp)

for i in range(len(patterns) - 1):
    for j in range(i + 1, len(patterns)):
        if patterns[i] == patterns[j]:
            ans += 1

print(ans)
