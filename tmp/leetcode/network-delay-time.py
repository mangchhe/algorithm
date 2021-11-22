import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        dist = [float('INF')]  * (n + 1)
        dist[k] = 0
        dist[0] = 0
        mv = defaultdict(list)
        for i in range(1, n + 1): mv[i] = []
        for t in times:
            mv[t[0]].append((t[2], t[1]))
        
        def traverse(start):
            h = [(0, start)]  
            
            while h:
                dis, node = heapq.heappop(h)

                if dist[node] < dis:
                    continue
                
                for i in mv[node]:
                    if dist[i[1]] > dis + i[0]:
                        dist[i[1]] = dis + i[0]
                        heapq.heappush(h, (dist[i[1]], i[1]))
                        
        
        traverse(k)
    
        ans = max(dist)
        
        if ans == float('INF'):
            return -1
        else:
            return ans
