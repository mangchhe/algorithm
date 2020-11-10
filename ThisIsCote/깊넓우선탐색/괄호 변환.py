"""
    작성일 : 20/11/10
"""

def solution(p):

    left, right = 0, 0
    count = 0
    s = []

    for i in p:
        if i == '(':
            left += 1
            if left > right:
                s.append('(')
            elif left == right:
                s.append('(' * count + ')' * count)
                count = 0
        else:
            right += 1
            if left >= right:
                s.append(')')
            else:
                count += 1

    return ''.join(s)

print(solution(')('))
