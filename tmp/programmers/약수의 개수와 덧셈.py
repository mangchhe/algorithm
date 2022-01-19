def solution(left, right):
    ans = 0
    for i in range(left, right + 1):
        if int(i ** .5) ** 2 == i:
            ans -= i
        else:
            ans += i
    return ans
