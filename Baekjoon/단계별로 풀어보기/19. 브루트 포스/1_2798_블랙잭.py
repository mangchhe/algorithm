from sys import stdin

N, M = map(int, stdin.readline().split())

NList = list(map(int, stdin.readline().split()))

result = []

for i in range(0, N - 2):

    for j in range(i + 1, N - 1):

        for k in range(j + 1, N):

            tmp = NList[i] + NList[j] + NList[k]

            if tmp > M:

                continue

            else:
                result.append(M - tmp)

print(M - min(result))