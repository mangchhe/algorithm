def solution(s):
    answer = ''
    numDic = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    tmpStr = ''

    for ss in s:
        if tmpStr and tmpStr in numDic:
            answer += numDic[tmpStr]
            tmpStr = ''
        if 48 <= ord(ss) <= 57:
            answer += ss
        else:
            tmpStr += ss

    if tmpStr:
        answer += numDic[tmpStr]

    return int(answer)


print(solution("one4seveneight"))