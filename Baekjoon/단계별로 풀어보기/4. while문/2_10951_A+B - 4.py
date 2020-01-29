A = -1
B = -1
while True:
    try:
        A, B = map(int, input().split())
    except EOFError:
        pass
    if A == 0 and B == 0:
        break
    print(A+B)

#import sys
#for line in sys.stdin:
#    n, k= map(int, line.split())