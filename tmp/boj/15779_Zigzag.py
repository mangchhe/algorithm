N = int(input())
arr = list(map(int, input().split()))
tmp = [2] * len(arr)

for i in range(2, len(tmp)):
    if not (arr[i - 2] <= arr[i - 1] and arr[i - 1] <= arr[i]) and not (arr[i - 2] >= arr[i - 1] and arr[i - 1] >= arr[i]):
        tmp[i] = tmp[i - 1] + 1

print(max(tmp))
