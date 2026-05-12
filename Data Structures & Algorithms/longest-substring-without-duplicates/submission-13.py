class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        char_s = set()
        for r in range(len(s)):
            while s[r] in char_s:
                char_s.remove(s[l])
                l += 1
            char_s.add(s[r])
            res = max(res, len(char_s))
        return res
            