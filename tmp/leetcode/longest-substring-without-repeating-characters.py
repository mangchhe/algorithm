# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 방법 1

def lengthOfLongestSubstring(s):
    wordCnt = {}
    cnt = 0
    l, r = 0, 0
    ans = 0
    while r < len(s):
        if not wordCnt.get(s[r]):
            cnt += 1
            wordCnt[s[r]] = 1
            r += 1
            ans = max(ans, cnt)
        else:
            for i in range(l, r):
                if s[r] != s[i]:
                    del wordCnt[s[i]]
                    cnt -= 1
                else:
                    del wordCnt[s[i]]
                    cnt -= 1
                    l = i + 1
                    break
    return ans

# 방법 2

def lengthOfLongestSubstring(s):
    wordCnt = {}
    l, r = 0, 0
    ans = 0
    while r < len(s):
        if not wordCnt.get(s[r]):
            wordCnt[s[r]] = 1
            r += 1
            ans = max(ans, len(wordCnt))
        else:
            del wordCnt[s[l]]
            l += 1
    return ans
