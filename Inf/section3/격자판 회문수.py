import sys

# sys.stdin = open('input.txt', 'rt')

data = []
res = 0

for i in range(7):
    data.append(input().split())

def isPalindrome(arr):
    arr2 = arr[::-1]

    for i in range(5):
        if arr[i] != arr2[i]:
            break
    else:
        return True
    
    return False

for i in range(7):
    s, e = 0, 5
    for _ in range(3):
        tmpArr = []
        tmpArr2 = []
        for j in range(s, e):
            tmpArr.append(data[i][j])
            tmpArr2.append(data[j][i])
        if isPalindrome(tmpArr):
            res += 1
        if isPalindrome(tmpArr2):
            res += 1
        s += 1
        e += 1

print(res)