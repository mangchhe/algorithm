# https://www.acmicpc.net/problem/2729

for _ in range(int(input())):
    print(bin(sum(map(lambda x : int(x, 2), input().split())))[2:])
