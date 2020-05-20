from sys import stdin

N = int(stdin.readline())

NList = []

NList_rank = []

for i in range(N):

    NList.append(list(map(int, stdin.readline().split())))

NList_rank.append(1)

for i in range(1, len(NList)):

    for j in range(1, len(NList)+1):

        try:
            idx = NList_rank.index(j)
            if NList[i][0] > NList[idx][0] and NList[i][1] > NList[idx][1]:
                for k in range(len(NList_rank)):
                    NList_rank[k] += 1
                NList_rank.append(j)
                break
            elif NList[i][0] < NList[idx][0] and NList[i][1] < NList[idx][1]:
                if j == max(NList_rank):
                    NList_rank.append(j + NList_rank.count(j))
                    break
            else:
                NList_rank.append(j)
                break
        except:
            pass

for val in NList_rank:

    print(val, end=' ')