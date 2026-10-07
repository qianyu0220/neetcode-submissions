class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        output = 0
        left, right = 0, n-1
        while left <= right:
            if heights[left] < heights[right]:
                water = (right - left) * heights[left]
                left += 1
            else:
                water = (right - left) * heights[right]
                right -= 1
            output = max(output, water)
        return output