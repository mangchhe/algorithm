def solution(numbers):
    ans = 45
    
    for num in numbers:
        ans -= num

    return ans
