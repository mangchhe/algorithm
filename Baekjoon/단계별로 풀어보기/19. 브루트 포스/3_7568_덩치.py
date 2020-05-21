from sys import stdin

N = int(stdin.readline())

NList = []
NList_rank = []

for i in range(N):
    NList.append(list(stdin.readline().split()))

for i in range(N):

    rank = 1

    for j in range(N):

        if j == i:

            pass

        else:

            if NList[i][0] < NList[j][0] and NList[i][1] < NList[j][1]:

                rank += 1

            else:

                pass

    NList_rank.append(rank)

for i in NList_rank:

    print(i, end=' ')