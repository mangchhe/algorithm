"""
    작성자 : 20/10/07
"""

""" 재귀 """

def fibo(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

""" 동적 """

memo = [0] * 101

def fibo2(n):

    if n == 1 or n == 2:
        return 1
    
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fibo2(n-1) + fibo2(n-2)
        return memo[n]

print(fibo2(100))