A, B, C = map(int, input().split())

modVal = []
val = []

def solve(N):

    global result
    tmp = N % C

    if tmp in modVal:
        pass
    else:
        modVal.append(tmp)
        val.append(N)
        solve(N*A)

solve(A)

if A < C:
    if A < C and B < C:
        del modVal[0]
    print(modVal[(B % len(modVal)) - 1])
else:
    print(modVal[(B % len(modVal)) - 1])