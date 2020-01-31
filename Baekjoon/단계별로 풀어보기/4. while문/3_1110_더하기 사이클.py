N = input()

tmp = N
count = 0

if len(N) == 1:
    N = '0' + N
    tmp = '0' + tmp

while True:
    try:
        tmp = tmp[1] + (str(int(tmp[0]) + int(tmp[1])))[1]
    except IndexError:
        tmp = tmp[1] + (str(int(tmp[0]) + int(tmp[1])))[0]
    count += 1
    if tmp == N:
        break

print(count)