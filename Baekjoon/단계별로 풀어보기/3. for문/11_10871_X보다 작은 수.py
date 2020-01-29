A, X = map(int, input().split())

XList = list(map(int, input().split()))

for i in range(A):
    if XList[i] < X:
        print(XList[i], end = ' ')
