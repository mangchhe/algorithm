# https://ko.wikipedia.org/wiki/%EC%8A%88%ED%8A%B8%EB%9D%BC%EC%84%BC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

processtion1 = []
processtion2 = []
result = []

N, M = map(int, input().split())

for i in range(N):
    processtion1.append(list(map(int, input().split())))

M, K = map(int, input().split())

for i in range(M):
    processtion2.append(list(map(int, input().split())))

for i in range(N):
    tmp = []
    for j in range(K):
        tmp2 = []
        for k in range(M):
            tmp2.append(processtion1[i][k] * processtion2[k][j])
        tmp.append(sum(tmp2))
    result.append([])
    result[i].extend(tmp)

for i in result:
    for j in i:
        print(j, end=' ')
    print()