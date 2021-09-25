# https://www.acmicpc.net/problem/1476

# 방법 1

input = __import__('sys').stdin.readline

E, S, M = map(int, input().split())
e, s, m = 0, 0, 0
year = 0

while True:
    e = e + 1 if e < 15 else 1
    s = s + 1 if s < 28 else 1
    m = m + 1 if m < 19 else 1
    year += 1

    if (e, s, m) == (E, S, M):
        print(year)
        break

# 방법 2

E, S, M = map(int, input().split())
year = 1

while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        print(year)
        break
    year += 1
