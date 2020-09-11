""" 
    작성일 : 20/09/11
"""

""" def solution(number, k):
    idx = 0
    number = list(number) <- 백만자리의 숫자를 list로 변경해야됨(시간 초과)
    length = len(number)
    for i in range(k):
        for j in range(idx, length - 1):
            if number[j] < number[j + 1]:
                idx = j - 1 if j > 0 else j
                del number[j]
                length -= 1
                break
            if j == length - 2:
                for l in range(k-i):
                    del number[j+1-l]
                return ''.join(number)

    return ''.join(number) """

def solution(number, k):
    idx = 0
    length = len(number)
    for i in range(k):
        for j in range(idx, length - 1):
            if number[j] < number[j + 1]:
                idx = j - 1 if j > 0 else j
                number = number.replace(number[j], '', 1)
                length -= 1
                break
            if j == length - 2:
                for l in range(k-i):
                    number = number.replace(number[j+1-l], '', 1)
                return ''.join(number)

    return ''.join(number)

print(solution('111119', 3))
print(solution('91111', 2))
print(solution('99991', 3))
print(solution('4177252841', 4))