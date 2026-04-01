class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqs = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key, occurs in count.items():
            freqs[occurs].append(key)

        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for freq in freqs[i]:
                if len(res) == k:
                    return res
                res.append(freq)
        return res