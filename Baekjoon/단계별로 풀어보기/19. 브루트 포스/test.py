def solution(name_list):

    findStr = name_list[0]

    for i in range(1, len(name_list)):

        if name_list[i].find(findStr) == -1:

            continue

        else:

            return True

    return False

if __name__ == '__main__':

    NList = input().split()

    print(solution(NList))