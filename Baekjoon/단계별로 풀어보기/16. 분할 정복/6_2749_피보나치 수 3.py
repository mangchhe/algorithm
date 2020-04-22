N = int(input())

c = 15 * (10 ** 5)

memo = {0:0,1:1,2:1}

if __name__ == '__main__':

    for i in range(2, c):

        memo[i] = (memo[i-1] + memo[i-2]) % 1000000


    print(memo[N % c])