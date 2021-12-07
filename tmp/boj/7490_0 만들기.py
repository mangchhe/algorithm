# # 방법1
def traverse(n, text):
    if n == N:
        if eval(text.replace(' ', '')) == 0:
            print(text)
        return
    traverse(n + 1, text + ' ' + str(n + 1))
    traverse(n + 1, text + '+' + str(n + 1))
    traverse(n + 1, text + '-' + str(n + 1))

for _ in range(int(input())):
    N = int(input())
    n = 1
    text = '1'
    traverse(n, text)
    print()

# 방법2
def traverse(n, sum, op, val, text):
    if n == N:
        sum += val * op
        if sum == 0:
            print(text)
        return
    traverse(n + 1, sum, op, val * 10 + n + 1, text + ' ' + str(n + 1))
    traverse(n + 1, sum + val * op, 1, n + 1, text + '+' + str(n + 1))
    traverse(n + 1, sum + val * op, -1, n + 1, text + '-' + str(n + 1))

for _ in range(int(input())):
    N = int(input())
    traverse(1, 0, 1, 1, '1')
    print()
