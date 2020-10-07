"""
    작성자 : 20/10/07
"""

""" 재귀 """

def fibo(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

""" 동적 Top-down """

memo = [0] * 151

def fibo2(n):
    if n == 1 or n == 2:
        return 1
    
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fibo2(n-1) + fibo2(n-2)
        return memo[n]

""" 동적 Bottom-up """

def fibo3(n):
    
    d = [0] * 151

    d[1] = 1
    d[2] = 1

    for i in range(3, n + 1):
        d[i] = d[i-1] + d[i-2]

    return d[n]

print(fibo(6))
print(fibo2(150))
print(fibo3(150))