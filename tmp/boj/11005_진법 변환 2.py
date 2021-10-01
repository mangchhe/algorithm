# https://www.acmicpc.net/problem/11005

input = __import__('sys').stdin.readline

def notation_converter(n, b):
    res = ''
    while n > 0:
        s = n % b
        if s < 10:
            res += str(s)
        else:
            res += chr(s + 55)
        n //= b
    return res[::-1]

N, B = map(int, input().split())

print(notation_converter(N, B))
