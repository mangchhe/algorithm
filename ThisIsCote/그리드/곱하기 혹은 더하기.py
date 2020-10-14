"""
    작성자 : 20/10/14
"""

s = list(map(int, list(input())))

sum = s[0]
del s[0]

for i in s:
    if sum + i < sum * i:
        sum *= i
    else:
        sum += i

print(sum)