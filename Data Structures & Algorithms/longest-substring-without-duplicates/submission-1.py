class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        s = list(s)
        l, r = 0, 1
        longest = 1
        curr_s = [s[l]]
        while r < len(s):
            if s[r] in curr_s:
                while s[l] != s[r]:
                    l += 1
                l += 1
                longest = max(longest, len(curr_s))
                curr_s = s[l:r + 1]
            else:
                curr_s.append(s[r])
            r += 1
        longest = max(longest, len(curr_s))
        return longest
            