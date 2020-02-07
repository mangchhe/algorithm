N = input().split()
A = list(N[0])
B = list(N[1])

AVal = 0
BVal = 0

for i in range(len(A)):
    AVal += int(A[i]) * (10 ** i)

for i in range(len(B)):
    BVal += int(B[i]) * (10 ** i)

if AVal > BVal:
    print(AVal)
else:
    print(BVal)

# 슬라이싱
# A = int(A[::-1])
# B = int(B[::-1])