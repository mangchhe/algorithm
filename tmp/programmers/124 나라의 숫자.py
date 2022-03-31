def solution(n):
    ans = ''
    while n > 0:
        tmp = n % 3
        if tmp == 0:
            ans += '4'
        else:
            ans += str(tmp)
        n = n // 3 - (n % 3 == 0)
    return ans[::-1]
