A, B = input().split()

if len(A) > len(B):
    A, B = B, A

_min = 50
for i in range(len(B) - len(A) + 1):
    tmp = 0
    for j in range(len(A)):
        if A[j] != B[j + i]:
            tmp += 1

    _min = min(_min, tmp)

print(_min)
