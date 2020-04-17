from sys import stdin

A, B, C = map(int, stdin.readline().split())

def solve(N):

    if N == 0:
        return 1
    else:
        tmp = solve(N//2)

        if N % 2 == 0:
            return tmp * tmp
        else:
            return tmp * tmp * A

print(solve(B) % C)
