input = __import__("sys").stdin.readline


def next_permutation(s):

    i = len(s) - 2
    j = 0

    while i > -1 and ord(s[i]) >= ord(s[i + 1]):
        i -= 1

    if i == -1:
        return s
    else:
        j = i + 1
        for k in range(j, len(s)):
            if ord(s[i]) < ord(s[k]):
                j = k
        s[i], s[j] = s[j], s[i]
        return s[: i + 1] + list(reversed(s[i + 1 :]))


for _ in range(int(input())):

    data = list(input().rstrip())

    print("".join(next_permutation(data)))
