# 방법 1

S = list(input())

T = 0

for i in range(len(S)):
    for j in range(65,91):
        if S[i] == chr(j):
            if j > 86:
                T += 10
                break
            elif j > 83:
                T += 9
                break
            elif j > 79:
                T += 8
                break
            T += ((j - 62) // 3) + 2
            break
print(T)

# 방법 2

mapping = [
    [],
    [],
    [],
    ["A","B","C"],
    ["D","E","F"],
    ["G","H","I"],
    ["J","K","L"],
    ["M","N","O"],
    ["P","Q","R","S"],
    ["T","U","V"],
    ["W","X","Y","Z"]
    ]
word = input()
answer = 0
for w in word:
    for i, alpha in enumerate(mapping):
        if w in alpha:
            answer += i
print(answer)