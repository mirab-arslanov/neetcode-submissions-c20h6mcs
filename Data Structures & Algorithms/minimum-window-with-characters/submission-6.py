class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        window, countT = {}, {}
        for let in t:
            countT[let] = 1 + countT.get(let, 0)
        
        res, res_len = (-1, -1), float('infinity')
        need, have = len(countT), 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res = (l, r)
                    res_len = r - l + 1
                le = s[l]
                window[le] -= 1
                if le in countT and window[le] < countT[le]:
                    have -= 1
                l += 1
        l, r = res[0], res[1] + 1
        return s[l:r] if res_len != float('infinity') else ''
                


            