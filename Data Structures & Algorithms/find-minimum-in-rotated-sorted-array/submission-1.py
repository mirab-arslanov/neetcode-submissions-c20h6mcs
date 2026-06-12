class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r] or len(nums) < 2:
            return nums[l]
        while r > l:
            if nums[r - 1] > nums[r]:
                return nums[r]
            r -= 1
