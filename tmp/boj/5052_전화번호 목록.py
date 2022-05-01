import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    ans = 'YES'
    phoneNumbers = [input().rstrip() for _ in range(N)]
    phoneNumbers.sort()

    for i in range(N - 1):
        if phoneNumbers[i] == phoneNumbers[i + 1][:len(phoneNumbers[i])]:
            ans = 'NO'
            break

    print(ans)
