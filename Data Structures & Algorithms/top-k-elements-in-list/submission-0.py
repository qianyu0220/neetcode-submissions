class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums = set(nums)
        nums_new = []
        output = []
        for num in nums:
            nums_new.append(num)
        for i in range(1, k+1):
            output.append(nums_new[-i])
        return output

