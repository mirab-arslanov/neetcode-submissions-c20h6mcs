class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))
        prev, pos = 1, 1
        for i in range(len(nums)):
            res[i] = prev
            prev *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pos
            pos *= nums[i]
        return res
            
        
