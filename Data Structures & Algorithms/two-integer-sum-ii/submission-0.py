class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [numbers[left], numbers[right]]
            elif total < target:
                left += 1
            else:
                right -= 1