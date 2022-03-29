def solution(board, skill):
    h, w = len(board), len(board[0])
    imos = [[0] * (w + 1) for _ in range(h + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        p = degree
        if type == 1:
            p = -p
            
        imos[r1][c1] += p
        imos[r1][c2 + 1] += -p
        imos[r2 + 1][c1] += -p
        imos[r2 + 1][c2 + 1] += p
        
    for i in range(w):
        for j in range(h):
            imos[j][i + 1] += imos[j][i]
    
    for i in range(h):
        for j in range(w):
            imos[i + 1][j] += imos[i][j]
            
    ans = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] + imos[i][j] > 0:
                ans += 1
        
    return ans
