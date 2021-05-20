# 방법 1
# def solution(N, number):

#     dp = [set() for _ in range(8)]

#     for i in range(8):
#         dp[i].add(int(str(N) * (i + 1)))
#         for j in range(i):
#             for op1 in dp[j]:
#                 for op2 in dp[i - j - 1]:
#                     dp[i].add(op1 + op2)
#                     dp[i].add(op1 - op2)
#                     dp[i].add(op1 * op2)
#                     if op2 != 0:
#                         dp[i].add(op1 // op2)

#         if number in dp[i]:
#             return i + 1

#     return -1

# 방법 2
answer = float('INF')


def dfs(N, number, cnt, sum):

    global answer

    if cnt > 9:
        return

    if sum == number:
        answer = min(cnt, answer)
    else:
        op = 0
        for i in range(9):
            op = op * 10 + N
            dfs(N, number, cnt + 1 + i, sum + op)
            dfs(N, number, cnt + 1 + i, sum - op)
            dfs(N, number, cnt + 1 + i, sum * op)
            if sum != 0:
                dfs(N, number, cnt + 1 + i, sum // op)


def solution(N, number):

    dfs(N, number, 0, 0)

    if answer == float('INF'):
        return -1

    return answer


print(solution(5, 12))