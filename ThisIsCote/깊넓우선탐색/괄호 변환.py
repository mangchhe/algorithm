"""
    작성일 : 20/11/10
"""

def correct_balance(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            length = len(s) // 2
            return '(' * length + ')' * length

    return s
    
def solution(p):
    
    b_s = ''
    a_s = ''
    left = 0
    right = 0

    for i in p:
        if i == '(':
            left += 1
            a_s += '('
        else:
            right += 1
            a_s += ')'
        if left == right:
            b_s += correct_balance(a_s)
            a_s = ''
            left, right = 0, 0

    return b_s

print(solution('()))((()'))
