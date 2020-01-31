N = 1
NCount = [0 for i in range(10)]

for i in range(3):
    N *= int(input())

while N > 0:
    tmp = N%10
    NCount[tmp]+=1
    N //= 10

for i in range(10):
    print(NCount[i])