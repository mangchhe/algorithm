timeList = []
min_time = 0
result = 0

for _ in range(int(input())):
    timeList.append(list(map(int, input().split())))

timeList = list(zip(*timeList))
timeList[0] = list(timeList[0])
timeList[1] = list(timeList[1])

while timeList[0]:
    if min_time <= timeList[0][0]:
        min_time = timeList[1][0]
        del timeList[0][0]
        del timeList[1][0]
        result += 1

    else:
        del timeList[0][0]
        del timeList[1][0]

print(result)

'''
while timeList[0]:
    time = 2147483647
    if min_time <= min(timeList[0]):
        for _ in range(timeList[0].count(min(timeList[0]))):
            idx = timeList[0].index(min(timeList[0]))
            if timeList[1][idx] - timeList[0][idx] < time:
                time = timeList[1][idx] - timeList[0][idx]
                min_time = timeList[1][idx]
            del timeList[0][idx]
            del timeList[1][idx]
        result += 1
    else:
        idx = timeList[0].index(min(timeList[0]))
        del timeList[0][idx]
        del timeList[1][idx]

print(result)
'''