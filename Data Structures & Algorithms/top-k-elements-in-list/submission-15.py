class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqs = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, i in count.items():
            freqs[i].append(num)
        
        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res