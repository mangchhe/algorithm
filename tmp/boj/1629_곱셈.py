def dac(n, k):
    if k == 0:
        return 1

    tmp = dac(n, k // 2)
    result = tmp ** 2 % C

    if k % 2:
        result = result * n % C

    return result



A, B, C = map(int, input().split())

print(dac(A, B))
