from sys import stdin

respo = {1:1,2:1,3:1}

def wave(N):

    if N not in respo:
        respo[N] = wave(N-2) + wave(N-3)

    return respo[N]

for i in range(int(input())):

    print(wave(int(stdin.readline().strip())))