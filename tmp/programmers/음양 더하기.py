def solution(absolutes, signs):
    ans = 0
    for val, sign in zip(absolutes, signs):
        sign = 1 if sign else -1
        ans += val * sign
    return ans
