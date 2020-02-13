#1
#7    6
#19   12
#37   18
#61   24
#등비수열
#ar**n-1
#등비수열의 합
#a * 1-r**n / 1-r

N = int(input())

i = 1
val = 1

while True:
    if val >= N:
        print(i)
        break
    else:
        val += 6 * i
        i += 1
