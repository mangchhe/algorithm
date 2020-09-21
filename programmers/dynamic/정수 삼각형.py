"""
    작성일 : 20/09/21
"""

def solution(triangle):

    length = len(triangle)

    for i in range(1, length):
        for j in range(0, 1 + i):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == 2 + i - 2:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                if triangle[i - 1][j - 1] > triangle[i - 1][j]:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += triangle[i - 1][j]

    return max(triangle[length - 1])

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])