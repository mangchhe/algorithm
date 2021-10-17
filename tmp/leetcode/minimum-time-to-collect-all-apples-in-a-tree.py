# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution(object):
    node = defaultdict(list)
    visited = [0] * (10**5 + 1)

    def init(self, edges):
        for edge in edges:
            self.node[edge[0]].append(edge[1])
            self.node[edge[1]].append(edge[0])

    def dfs(self, hasApple, now):
        self.visited[now] = 1
        if not self.node[now]:
            if hasApple[now]:
                return 2
            else:
                return 0
        else:
            total = 0
            for i in self.node[now]:
                if not self.visited[i]:
                    total += self.dfs(hasApple, i)
            return total + 2 if hasApple[now] or total > 0 else 0

    def minTime(self, n, edges, hasApple):
        self.node = defaultdict(list)
        self.visited = [0] * (10**5 + 1)
        self.init(edges)
        ans = self.dfs(hasApple, 0)
        return ans - 2 if ans > 0 else 0
