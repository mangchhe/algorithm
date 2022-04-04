k = int(input()) + 1
n = 0
ans = 0
possible = True

while k > 0:
    if n > 9876543210:
        possible = False
        break
    tmp = n
    cnt = 0
    digit = -1
    while tmp > 0:
        if tmp % 10 > digit:
            digit = tmp % 10
            cnt += 1
        else:
            n = (tmp + 1) * (10 ** cnt)
            break
        tmp //= 10
    else:
        ans = n
        n += 1
        k -= 1

if possible:
    print(ans)
else:
    print(-1)
