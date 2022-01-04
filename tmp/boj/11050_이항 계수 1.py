# 이항계수
# - 이항식을 이항정리를 전개했을 때 각 항의 계수를 나타냄
# - (x + y)^2 = x^2 + 2xy + y^2 = [1, 2, 1]
# - 조합(combination)으로 구할 수 있고 nCk = n!/(n - k)!k!

def factorial(n):
    if n < 1:
        return 1
    return factorial(n - 1) * n

N, K = map(int, input().split())

print(factorial(N) // (factorial(N - K) * factorial(K)))
