""" 
    작성일 : 20/09/11
"""

""" count = 0 # 실패 코드

def solution(numbers, target):

    solution2(1, len(numbers), target,0)

    return count

def solution2(number, iterations, target, result):

    global count

    print(number, result, iterations)

    result += number
    iterations -= 1

    if iterations == 0:
        if result == target:
            count += 1
    else:
        if number == 1:
            solution2(-1, iterations, target, result)
        if number == -1:
            solution2(1, iterations, target, result)
"""

def solution(numbers, target):

    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])

""" import copy # 가독성은 재귀가 좋지만 속도면에서는 밑에 소스가 더 빠름

def solution(numbers, target):

    count = 0

    tmp = [numbers[0],-numbers[0]]
    del numbers[0]

    for i in range(len(numbers)):
        tmp2 = []
        for j in tmp:
            tmp2.append(j + numbers[0])
            tmp2.append(j + -numbers[0])
        tmp = copy.copy(tmp2)
        del numbers[0]

    return len(list(filter(lambda x: x == target, tmp))) """

print(solution([1,1,1,1,1], 3))