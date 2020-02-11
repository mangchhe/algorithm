

alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

S = input()

# 방법 1 (index, replace)

i = 0

while True:
    try:
        S.index(alpha[i])
        S = S.replace(alpha[i],'0',1)
    except:
        i += 1
        if i == 8:
            break
print(len(S))

# 방법 2 (count)

sum = 0

for i in range(len(alpha)):
    sum += S.count(alpha[i])
    S = S.replace(alpha[i],'0')

S = S.replace('0','')
print(len(S) + sum)
