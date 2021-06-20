input = __import__('sys').stdin.readline

N = int(input())

cnt = N // 5
ans = 0

while True:
    tmp = N - 5 * cnt
    if tmp > N:
        ans = -1
        break
    if tmp % 2 == 0:
        ans += cnt
        ans += tmp // 2
        break
    else:
        cnt -= 1

print(ans)
