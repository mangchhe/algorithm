from collections import defaultdict
import heapq

class Solution(object):
        
    def findTheCity(self, n, edges, distanceThreshold):
        
        ans = (0, float('INF'))
        route = defaultdict(list)
        dis = []
    
        def dijkstra(start, distanceThreshold):
        
            dis[start] = 0
            h = [(0, start)]

            while h:
                dist, now = heapq.heappop(h)

                if dis[now] < dist:
                    continue

                for i in route[now]:
                    if dist + i[1] < dis[i[0]] and dist + i[1] <= distanceThreshold:
                        dis[i[0]] = dist + i[1]
                        heapq.heappush(h, (dis[i[0]], i[0]))
        
        for edge in edges:
            a, b, c = edge
            route[a].append((b, c))
            route[b].append((a, c))
        
        for i in range(n):
            dis = [float('INF')] * n
            dijkstra(i, distanceThreshold)
            length = len(filter(lambda x: x != float('INF'), dis))
            if length <= ans[1]:
                ans = (i, length)
                
        return ans[0]

