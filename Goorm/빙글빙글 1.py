N = int(input())

NList = [[' ' for i in range(N * 2)] for j in range(N * 2)]

xPos = yPos = 0

num = 2

for i in range(N, 0):

    for j in range(0, i):

        xPos += num * j

        NList[xPos][yPos] = '#'

    if i == 1:
        break

    for k in range(0, i):

        yPos += num * k

        NList[xPos][yPos] = '#'

    num *= -1

print(NList)