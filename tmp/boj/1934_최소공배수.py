# 유클리드 호제법 : 최대공약수 구하기
def euclidean(a, b):
    if b == 0:
        return a

    return euclidean(b, a % b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    gcd = euclidean(a, b)
    print((a // gcd) * b)

