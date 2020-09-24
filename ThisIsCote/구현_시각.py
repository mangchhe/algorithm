""" 
    작성일 : 20/09/24
"""

count = 0

n = int(input())

for i in range(60):
    for j in range(60):
        if '3' in str(i) + str(j):
            count += 1

print(((n - (n // 3) + 1) * count) + ((n // 3) * 60 * 60))

""" for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count) """

