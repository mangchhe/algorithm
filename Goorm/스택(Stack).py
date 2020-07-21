from sys import stdin

stackList = []

for i in range(int(stdin.readline())):

    msg = int(stdin.readline())

    if msg == 1:

        if not stackList:

            print('underflow')

        else:

            stackList.pop()

    elif msg == 0:

        if len(stackList) == 10:

            print('overflow')

        else:

            stackList.append(int(stdin.readline()))

    else:

        break

for i in stackList:
    print(i, end=' ')

