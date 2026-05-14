class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        window, countT = {}, {}
        for let in t:
            countT[let] = 1 + countT.get(let, 0)
        
        res = (-1, -1), float('infinity')
        need, have = len(countT), 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT:
                have += 1 if window[c] == countT[c] else 0
            while have == need:
                res = ((l, r), r - l + 1) if r - l + 1 < res[1] else res
                le = s[l]
                window[le] -= 1
                if le in countT:
                    have -= 1 if window[le] < countT[le] else 0
                l += 1
        l, r = res[0][0], res[0][1] + 1
        return s[l:r] if res[1] != float('infinity') else ''
                


            