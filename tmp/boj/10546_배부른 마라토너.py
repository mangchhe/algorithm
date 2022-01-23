input = __import__('sys').stdin.readline

N = int(input())
names = {}

for i in range(N):
    s = input()
    names[s] = names.get(s, 0) + 1

for i in range(N - 1):
    s = input()
    if names[s] - 1 == 0:
        del names[s]
    else:
        names[s] -= 1

for ans in names.keys():
    print(ans)
