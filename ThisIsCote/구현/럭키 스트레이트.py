"""
    작성일 : 20/10/15
"""

n = input()

length = len(n)

left = 0
right = 0

for i in range(length):
    if i // (length // 2) < 1:
        left += int(n[i])
    else:
        right += int(n[i])

if left == right:
    print('LUCKY')
else:
    print('READY')
