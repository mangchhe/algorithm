'''

N = int(input())

box = [[' ' for j in range(N * 2)] for i in range(N)]

def solve(n, x, y):

    if n == 3:

        box[x][y] = '*'
        box[x + 1][y - 1] = '*'
        box[x + 1][y + 1] = '*'
        box[x + 2][y - 2] = '*'
        box[x + 2][y - 1] = '*'
        box[x + 2][y] = '*'
        box[x + 2][y + 1] = '*'
        box[x + 2][y + 2] = '*'

    else:

        solve(n//2, x, y)
        solve(n//2, x + n//2, y - n//2)
        solve(n//2, x + n//2, y - n//2 + n)

solve(N, 0 , N - 1)

for i in box:

    for j in i:

        print(j, end='')

    print('')

'''

block = ["  *  ", " * * ", "*****"]

N = int(input())

for i in range(11):

    idx = 3 * 2 ** i

    if idx > N:
        break
    elif idx == 3:
        continue

    length = len(block)

    for j in range(length):
        block.append(block[j] + " " + block[j])
        block[j] = " " * (idx // 2) + block[j] + " " * (idx // 2)


for val in block:
    print(val)