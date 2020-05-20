from sys import stdin

N = stdin.readline()

N_current = int(N)

N_length = len(N)

result = 0

for i in range(1, N_length ** 3):

    N_current -= 1
    tmp_sum = 0
    tmp_current = N_current

    for j in range(N_length):

        tmp_sum += tmp_current % 10
        tmp_current //=  10

    tmp_sum += N_current

    if tmp_sum == int(N):

        result = N_current

print(result)