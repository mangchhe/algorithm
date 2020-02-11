N = int(input())

count = 0

for i in range(N):
    S = input()
    tmp = []
    for j in range(len(S)-1):
        if S[j] in tmp:
            break
        if S[j] == S[j+1]:
            pass
        else:
            tmp.append(S[j])
        if j == len(S)-2:
            if S[j+1] in tmp:
                break
            else:
                count += 1
    if len(S) == 1:
        count += 1

print(count)