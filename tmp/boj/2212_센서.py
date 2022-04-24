N = int(input())
K = int(input())

sensors = sorted(map(int, input().split()))
dis = []

for i in range(N - 1):
    dis.append(sensors[i + 1] - sensors[i])

dis.sort()

print(sum(dis[:N - 1 - (K - 1)]))
