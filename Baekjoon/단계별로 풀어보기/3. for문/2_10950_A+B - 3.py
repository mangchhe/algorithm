T = int(input())

val = []

for i in range(T):
    A, B = map(int, input().split())
    val.append(A+B)

for i in range(T):
    print(val[i])