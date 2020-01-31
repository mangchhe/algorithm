# 1. 기본 라이브러리 함수 이용

NList = []
for i in range(9):
    NList.append(int(input()))

print(max(NList))
print(NList.index(max(NList))+1)

# 2. 알고리즘 이용
max = 0
idx = 0

for i in range(1,10):
    val = int(input())
    if max < val:
        max = val
        idx = i

print(max)
print(idx)