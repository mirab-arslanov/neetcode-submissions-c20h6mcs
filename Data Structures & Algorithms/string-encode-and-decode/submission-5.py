class Solution:

    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return ''.join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            quant = s[i:s.find('#', i)]
            i += len(quant) + 1
            quant = int(quant) + i
            res.append(s[i:quant])
            i = quant
        return res
