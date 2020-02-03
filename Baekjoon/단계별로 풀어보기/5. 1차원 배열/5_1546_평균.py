sum = 0
maxNum = 0

num = int(input())
N = list(map(int, input().split()))

maxNum = max(N)

for i in range(num):
    N[i] = (N[i] / maxNum) * 100
    sum += N[i]

print(sum/num)