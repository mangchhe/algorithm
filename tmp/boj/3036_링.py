# 기약분수
# - 분모와 분자를 최대공약수로 약분하여 1 이외의 공약수를 갖지 않도록 만든 분수
# 원의 둘레 : 3.14 * r * 2
# 원의 넓이 : 3.14 * r ** 2

def euclidean(a, b):
    if b == 0:
        return a
    
    return euclidean(b, a % b)

N = int(input())
radius = list(map(int, input().split()))

for i in range(1, N):
    gcd = euclidean(radius[0], radius[i])
    print('{}/{}'.format(radius[0] // gcd, radius[i] // gcd))
