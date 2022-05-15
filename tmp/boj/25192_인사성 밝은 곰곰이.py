import sys
input = sys.stdin.readline

N = int(input())
ans = 0

users = {}
for chat in [input().rstrip() for _ in range(N)]:
    if chat == 'ENTER':
        users = {}
        continue

    if not users.get(chat):
        users[chat] = 1
        ans += 1

print(ans)
