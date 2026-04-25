class Solution:
    def maxArea(self, h: List[int]) -> int:
        # if max(h) == min(h):
        #     return h[0] * (len(h) - 1)
        
        most_water = 0
        l, r = 0, len(h) - 1
        while l < r:
            water = min(h[l], h[r]) * (r - l)
            most_water = max(most_water, water)
            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1
        return most_water