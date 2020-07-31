from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())

if A > 0 and B > 0:

    print(1)

elif A < 0 and B > 0:

    print(2)

elif A < 0 and B < 0:

    print(3)

else:

    print(4)