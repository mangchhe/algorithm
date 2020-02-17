# 1 3 6 10 15
# 1
# 1 + 2
# 1 + 2 + 3
# 1 + 2 + 3 + 4 .. (n-1) + n
# 1 3 6 10 15 21
# 등차수열의합 n(a+l) / 2
# n(n+1)/2
# (n**2 + n) / 2
# 계차수열 : 항간의 차이를 수열로 씀
# 그 차이가 일정할 경우 그 차이를 공차라고 부르고 원래 수열은 등차수열이 됨

N = int(input())

idx = 1
leftover = 0
x = 0
y = 0

while True:
    if N <= (idx * (idx+1)) // 2:
        leftover = N - ((idx-1) * ((idx-1)+1)) // 2 - 1
        break
    idx += 1

if idx % 2 == 0:
    x = 1 + leftover
    y = idx - leftover
else:
    x = idx - leftover
    y = 1 + leftover

print('{}/{}'.format(x,y))

