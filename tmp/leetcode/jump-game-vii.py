# https://leetcode.com/problems/jump-game-vii/

from collections import deque

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        q = deque([(minJump, maxJump)])
        now = minJump
        ans = 0
        while q and now < len(s):
            if q[0][1] < now:
                q.popleft()
                continue
            if now >= q[0][0]:
                if s[now] == '0' and now <= q[0][1]:
                    q.append((now + minJump, now + maxJump))
                    ans = now
            now += 1

        return True if ans == len(s) - 1 else False
