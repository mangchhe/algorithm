from sys import stdin, stdout

N = int(stdin.readline())

NList = []

# 방법 1
# for i in range(N):
#
#     NList.append(int(stdin.readline()))

# 방법 2
NList = [int(stdin.readline()) for _ in range(N)]

NList.sort()

# 방법 1
# for i in range(N):
#
#     print(NList[i])

# 방법 2
stdout.write('\n'.join(map(str, NList)))
