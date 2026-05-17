class Solution:
    def isValid(self, s: str) -> bool:
        op = ('[', '(', '{')
        cl = (']', ')', '}')
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] in op or not stack:
                stack.append(s[i])
            elif s[i] == ']' and stack[-1] != '[':
                return False
            elif s[i] == ')' and stack[-1] != '(':
                return False
            elif s[i] == '}' and stack[-1] != '{':
                return False
            else:
                stack.pop()
        return True if not stack else False
