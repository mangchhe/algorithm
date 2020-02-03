num = int(input())

for i in range(num):
    zum = 0
    sum = 0
    OX = input()
    for j in range(len(OX)):
        if OX[j] == 'O':
            zum += 1
        else:
            zum = 0
        sum += zum
    print(sum)

