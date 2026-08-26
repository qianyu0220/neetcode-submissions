class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = i + 1
            j = n - 1
            while k < j:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    k += 1
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
                elif total < 0:
                    k += 1
                else:
                    j -= 1
        return output
