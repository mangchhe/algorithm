ans = 0

prev_words = ['c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu']
next_word = 'aeiouh'

for s in input().replace('-', ' ').split():
    idx = s.find('\'')
    if idx != -1:
        for pw in prev_words:
            if pw == s[0:idx]:
                if s[idx + 1] in next_word:
                    ans += 1
    ans += 1

print(ans)
