def solution(info, edges):
    def traverse(sheep, wolf, current, path):
        if info[current]:
            wolf += 1
        else:
            sheep += 1
        
        if wolf >= sheep:
            return 0
        
        maxSheep = sheep
        
        for p in path:
            for now in graph[p]:
                if now in path:
                    continue
                path.append(now)
                maxSheep = max(maxSheep, traverse(sheep, wolf, now, path))
                path.pop()
            
        return maxSheep
    
    graph = {i : [] for i in range(len(info))}
    for edge in edges:
        a, b = edge
        graph[a].append(b) 
    
    return traverse(0, 0, 0, [0])
