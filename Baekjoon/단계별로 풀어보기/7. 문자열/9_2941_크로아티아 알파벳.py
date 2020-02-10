

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