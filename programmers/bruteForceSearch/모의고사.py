""" 
    작성일 : 20/09/09 - 완료
"""

def solution(answers):

    zzik = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    dap = [0, 0, 0]
    zzik_idx = [0, 0, 0]
    zzik_length = [len(zzik[0]), len(zzik[1]), len(zzik[2])]

    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == zzik[j][zzik_idx[j]]:
                dap[j] += 1
            zzik_idx[j] += 1
            if zzik_length[j] == zzik_idx[j]:
                zzik_idx[j] = 0

    result = [idx+1 for idx, val in enumerate(map(lambda x: x == max(dap), dap)) if val == True]

    return result

print(solution([1,3,2,4,2]))