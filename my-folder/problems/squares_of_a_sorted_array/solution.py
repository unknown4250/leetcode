class Solution(object):
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        idx = len(nums) - 1
        result = [0] * len(nums)

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[idx] = nums[left] * nums[left]
                idx -= 1
                left += 1
            else:
                result[idx] = nums[right] * nums[right]
                idx -= 1
                right -= 1
        return result
        