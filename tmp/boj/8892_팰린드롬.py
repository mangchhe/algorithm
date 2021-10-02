# https://www.acmicpc.net/problem/8892

input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N = int(input())
    nList = [input().rstrip() for _ in range(N)]
    ans = ''
    for i in range(len(nList) - 1):
        for j in range(i + 1, len(nList)):
            s1 = nList[i] + nList[j]
            s2 = nList[j] + nList[i]
            if s1 == s1[::-1]:
                ans = s1
            if s2 == s2[::-1]:
                ans = s2
        if ans:
            break

    print(ans if ans else 0)
