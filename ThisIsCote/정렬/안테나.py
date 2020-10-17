"""
    작성일 : 20/10/17
"""

n = int(input())
data = list(map(int, input().split()))

print(sorted(data)[len(data) // 2 - 1])