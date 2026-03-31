class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = sorted(nums)
        res, temp = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                temp += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                res = max(temp, res)
                temp = 1

        res = max(temp, res)
        return res