class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [1]
        freqs = [[] for _ in range(len(nums) + 1)]
        nums = sorted(nums)
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                freqs[count].append(nums[i - 1])
                count = 1
            else:
                count += 1
        freqs[count].append(nums[i])

        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for freq in freqs[i]:
                if len(res) == k:
                    return res
                res.append(freq)
        return res