class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))
        left, right = 1, 1
        n = len(nums)
        for i in range(n):
            output[i] = left
            left *= nums[i]
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output