def solve(place):
    pList = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                pList.append([i, j])

    while pList:
        nowX, nowY = pList.pop()
        for p in pList:
            x, y = p
            n = abs(nowX - x) + abs(nowY - y)
            if n > 2:
                pass
            else:
                if nowX == x:
                    if place[nowX][(nowY + y) // 2] == 'X':
                        pass
                    else:
                        return 0
                elif nowY == y:
                    if place[(nowX + x) // 2][nowY] == 'X':
                        pass
                    else:
                        return 0
                else:
                    if place[x][nowY] == 'X' and place[nowX][y] == 'X':
                        pass
                    else:
                        return 0

    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(solve(place))

    return answer


print(
    solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
