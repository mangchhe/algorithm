"""
    작성일 : 20/10/15
"""

s = input()

n = 0
result = ''

s = sorted(s)

for idx, i in enumerate(s):
    if ord(i) > 48 and ord(i) < 58:
        n += int(i)
    else:
        for j in range(idx, len(s)):
            result += s[j]
        result += str(n)
        break

print(result)