from string import punctuation


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()

        while left < right:
            if s[left] == ' ' or s[left] in punctuation:
                left += 1
                continue
            if s[right] == ' ' or s[right] in punctuation:
                right -= 1
                continue

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True