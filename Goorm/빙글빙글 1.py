N = int(input())

NList = [[' ' for i in range(N * 2)] for j in range(N * 2)]

xPos = yPos = 0

num = 2

for i in range(0, N):

    if i == N - 1:

        break

    if i == 0:

        for j in range(0, N - i - 1):

            NList[xPos][yPos] = '#'

            yPos += num

        for k in range(0, N - i - 1):
            NList[xPos][yPos] = '#'

            xPos += num

        for l in range(0, N - i - 1):

            NList[xPos][yPos] = '#'

            yPos -= num

    else:

        for k in range(0, N - i * 2 - 1):
            print(xPos)
            NList[xPos][yPos] = '#'

            xPos -= num

        for j in range(0, N - i * 2 - 1):

            NList[xPos][yPos] = '#'

            yPos += num


for i in NList:
    for j in i:
        print(j, end='')
    print()