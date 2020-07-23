from sys import stdin

A, op, B = stdin.readline().split()

A = int(A)
B = int(B)

if op == '+':

    print(A + B)

elif op == '-':

    print(A - B)

elif op == '*':

    print(A * B)

elif op == '/':

    print('%.2f' % (A / B))