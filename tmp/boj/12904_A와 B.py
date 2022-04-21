src = list(input())
target = list(input())

while len(src) < len(target):
    if target[-1] == 'A':
        target.pop()
    else:
        target.pop()
        target = target[::-1]

if src == target:
    print(1)
else:
    print(0)
