class Solution(object):
    def multiply(self, num1, num2):
#         ans = 0
#         cnt = 0
#         for i in range(len(num2) - 1, -1, -1):
#             cnt = len(num2) - 1 - i
#             for j in range(len(num1) - 1, -1, -1):
#                 ans += int(num2[i]) * int(num1[j]) * (10 ** cnt)
#                 cnt += 1

#         return str(ans)
        ans = 0
        cnt = 0
        for i in range(len(num2) -1, -1, -1):
            ans += int(num2[i]) * int(num1) * (10 ** cnt)
            cnt += 1
            
        return str(ans)
