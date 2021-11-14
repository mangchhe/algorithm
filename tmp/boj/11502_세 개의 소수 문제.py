input = __import__('sys').stdin.readline

cache = [0] * 10001
cache[0] = 1
cache[1] = 1
decimal = []
ans = ()

for i in range(2, int(10001 ** .5) + 1):
    for j in range(i * i, 10001, i):
        cache[j] = 1

for i in range(len(cache)):
    if cache[i] == 0:
        decimal.append(i)

for _ in range(int(input())):
    N = int(input())
    flag = False
    for i in range(len(decimal)):
        for j in range(len(decimal)):
            for k in range(len(decimal)):
                if decimal[i] + decimal[j] + decimal[k] == N:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    
    if ans:
        print(*ans)
    else:
        print(0)

