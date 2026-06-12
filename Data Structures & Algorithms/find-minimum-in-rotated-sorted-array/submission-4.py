class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums)
        # if nums[left] < nums[right - 1] or right < 2:
        #     return nums[left]

        while right > left:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[right - 1]:
                left = mid + 1
            else:
                right = mid
        return nums[mid]