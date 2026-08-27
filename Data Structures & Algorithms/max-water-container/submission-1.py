class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n-1
        water = 0
        output = 0
        while left < right:
            if heights[left] < heights[right]:
                water = (right - left) * heights[left]
                left += 1
            else:
                water = (right - left) * heights[right]
                right -= 1
            output = max(output, water)
        return output