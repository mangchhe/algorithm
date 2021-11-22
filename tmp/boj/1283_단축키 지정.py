input = __import__('sys').stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
visited = {i : 0 for i in range(26)}

for i in range(N):
    word_split = words[i].split()
    for j, word in enumerate(word_split):
        if not visited[ord(word_split[j][0].upper()) - 65]:
            visited[ord(word_split[j][0].upper()) - 65] = 1
            words[i] = ' '.join(word_split[:j] + ['[' + word_split[j][0] + ']' + word_split[j][1:]] + word_split[j + 1:])
            break
    else:
        for j, word in enumerate(words[i]):
            if word != ' ' and not visited[ord(word.upper()) - 65]:
                visited[ord(word.upper()) - 65] = 1
                words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j + 1:]
                break

for word in words:
    print(word)
