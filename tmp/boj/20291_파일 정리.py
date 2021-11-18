input = __import__('sys').stdin.readline

extension = {}

for _ in range(int(input())):
    s = input().rstrip().split('.')[1]
    extension[s] = extension.get(s, 0) + 1

for i in sorted(extension):
    print(i, extension[i])
