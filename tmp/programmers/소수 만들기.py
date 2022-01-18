def traverse(arr, sumNums, n, total, cnt):
    if cnt == 3:
        sumNums.append(total)
        return
    for i in range(n + 1, len(arr)):
        traverse(arr, sumNums, i, total + arr[i], cnt + 1)

def erathos(maxVal):
    isPrimes = [False] * (maxVal + 1)
    for i in range(2, int(maxVal ** .5) + 1):
        if isPrimes[i]:
            continue
        for j in range(i * i, maxVal + 1, i):
            isPrimes[j] = True
    return isPrimes
    
def solution(nums):
    ans = 0
    sumNums = []
    traverse(nums, sumNums, -1, 0, 0)
    isPrimes = erathos(max(sumNums))

    for num in sumNums:
        if not isPrimes[num]:
            ans += 1
            
    return ans
