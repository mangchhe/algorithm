"""
    작성일 : 20/11/08
"""

def solution(s):

    idx = 1
    s_length = len(s)
    result = s_length

    while idx < s_length // 2 + 1:

        length = s_length // idx
        tmp = ''
        count = 1
        before = s[0 * idx : 1 * idx]

        for i in range(1, length):
            if before == s[i * idx:(i + 1) * idx]:
                count += 1
            else:
                if count == 1:
                    tmp += before
                else:
                    tmp += str(count) + before
                before = s[i * idx:(i + 1) * idx]
                count = 1
            if i == length - 1:
                if count == 1:
                    tmp += before
                else:
                    tmp += str(count) + before

        tmp += s[(length)* idx :]
        idx += 1

        if len(tmp) < result:
            result = len(tmp)

    return result

solution('aabbaccc')