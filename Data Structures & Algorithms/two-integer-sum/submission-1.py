class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        output = []
        hashmap = {}
        for index, i in enumerate(nums):
            comple = target - i
            if comple in hashmap:
                return [hashmap[comple], index]
            hashmap[i] = index