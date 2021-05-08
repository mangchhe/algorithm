def solution(n, start, end, roads, traps):
    answer = 0

    map = [[0] * (n + 1) for _ in range(n + 1)]

    for road in roads:
        map[road[0]][road[1]] = road[2]

    return answer