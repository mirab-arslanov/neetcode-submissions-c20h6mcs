class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if max(heights) == min(heights):
            return heights[0] * (len(heights) - 1)
        max_pool = 0
        for i, a in enumerate(heights):
            for j, b in enumerate(heights):
                if i == j:
                    continue
                res = min(a, b) * (j - i)
                max_pool = max(max_pool, res)
        return max_pool