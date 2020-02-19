import math

N = int(input())

for i in range(N):
    H, W, N = map(int, input().split())
    print('{}{}'.format(N%H if N%H != 0 else H,math.ceil(N/H) if math.ceil(N/H) > 9 else '0'+ str(math.ceil(N/H))))
