from sys import stdin

N, M = map(int, stdin.readline().split())

flag = True

for i in range(N):

    if i % 2 == 0:

        print('#' * M)

    else:

        if flag:

            print(('.' * (M - 1)) + '#')
            flag = False

        else:

            print('#' + ('.' * (M - 1)))
            flag = True

