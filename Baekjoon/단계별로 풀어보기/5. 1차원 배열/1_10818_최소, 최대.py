# 1. 기본 라이브러리 함수 이용
tmp = input()

NList = list(map(int, input().split()))

print(min(NList),max(NList))

# 2. 알고리즘 이용
N = int(input())

min = 1000001
max = 0

NList = list(map(int, input().split()))

for val in NList:
    if val < min:
        min = val
    if val > max:
        max = val

print(min, max)