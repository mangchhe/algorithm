# 1
def dac(arr, s, e):
    if e - s <= 1:
        return

    n = (e - s) // 3

    for i in range(s + n, s + n * 2):
        arr[i] = ' '

    dac(arr, s, s + n)
    dac(arr, e - n, e)

def solve():
    N = int(input())
    arr = ['-'] * (3 ** N)
    dac(arr, 0, 3 ** N)
    return arr

while 1:
    try:
        print(''.join(solve()))
    except:
        break

# 2
def dac2(n):
    if n == 0:
        return '-'
    s = dac2(n - 1)
    return s + len(s) * ' ' + s

while 1:
    try:
        print(dac2(int(input())))
    except:
        break
