def dfs(idx, n, target, numbers, res):

    if idx >= len(numbers):
        if n == target:
            res[0] += 1
    else:
        dfs(idx + 1, n + numbers[idx], target, numbers, res)
        dfs(idx + 1, n - numbers[idx], target, numbers, res)


def solution(numbers, target):

    res = [0]
    dfs(0, 0, target, numbers, res)
    return res[0]


# 다른 사람 풀이 참고 소스

# def solution(numbers, target):

#     if not numbers and target == 0:
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target + numbers[0]) + solution(
#             numbers[1:], target - numbers[0])

print(solution([1, 1, 1, 1, 1], 3))