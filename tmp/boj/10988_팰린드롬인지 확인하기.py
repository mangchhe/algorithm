s = input()

mid = len(s) // 2

for i in range(0, mid):
    if s[i] != s[len(s) - 1 - i]:
        print(0)
        exit()

print(1)
