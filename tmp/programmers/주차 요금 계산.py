import math

def solution(fees, records):
    carRecord = {}
    for record in records:
        time, carNum, go = record.split()
        time = time.split(':')
        time = int(time[0]) * 60 + int(time[1])
        if carRecord.get(carNum):
            carRecord[carNum].append(time)
        else:
            carRecord[carNum] = [time]
            
    endTime = 23 * 60 + 59
    carTimeRecord = {}
    for carNum, times in carRecord.items():
        for i in range(0, len(times), 2):
            if i + 1 < len(times):
                carTimeRecord[carNum] = carTimeRecord.get(carNum, 0) + times[i + 1] - times[i]
            else:
                carTimeRecord[carNum] = carTimeRecord.get(carNum, 0) + endTime - times[i]
    
    ans = []
    for carNum, time in sorted(carTimeRecord.items()):
        ans.append(math.ceil(max(0, time - fees[0]) / fees[2]) * fees[3] + fees[1])
        
    return ans
