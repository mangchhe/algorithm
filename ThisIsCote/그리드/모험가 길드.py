"""
    작성자 : 20/10/15
"""

n = int(input())
data = list(map(int, input().split()))
data = sorted(data)
length = len(data)
count = 0
i = 0

while True:
    i += data[i]
    if i > length - 1:
        break
    else:
        count += 1

print(count)