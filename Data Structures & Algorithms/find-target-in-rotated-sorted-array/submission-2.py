class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while r >= l:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if target < nums[l] or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            else:
                if target < nums[l] and nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
        return -1

            
        