N = int(input())
arr = sorted(map(int, input().split()))
ans = float('INF')
ansPos = [0, 0]

l, r = 0, len(arr) - 1

while l < r:
    water = arr[l] + arr[r]
    
    if abs(water) < ans:
        ans = abs(water)
        ansPos[0] = arr[l]
        ansPos[1] = arr[r]

        if water == 0:
            break

    if arr[l] + arr[r] < 0:
        l += 1
    else:
        r -= 1

print(ansPos[0], ansPos[1])
