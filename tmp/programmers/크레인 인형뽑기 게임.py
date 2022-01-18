def solution(board, moves):
    ans = 0
    bucket = []
    dolls = [[] for _ in range(len(board) + 1)]
    
    for i in range(len(board)):
        for j in range(len(board) - 1, -1, -1):
            doll = board[j][i]
            if doll:
                dolls[i + 1].append(doll)
                
    for move in moves:
        if not dolls[move]:
            continue
        doll = dolls[move].pop()
        if bucket:
            if bucket[-1] == doll:
                bucket.pop()
                ans += 2
                continue
        bucket.append(doll)
    
    return ans
