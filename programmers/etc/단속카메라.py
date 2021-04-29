# def solution(routes):
#     answer = 0
#     routes = sorted(routes, key=lambda x: x[1])
#     s, e = routes[0]
#     del routes[0]
#     answer += 1
#     for route in routes:
#         ss, ee = route
#         if ss <= e:
#             if e > ee:
#                 e = ee
#         else:
#             s = ss
#             e = ee
#             answer += 1

#     return answer


def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    e = -30000

    for route in routes:
        if e < route[0]:
            answer += 1
            e = route[1]

    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
