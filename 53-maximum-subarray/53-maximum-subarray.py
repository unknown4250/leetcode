class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        result = [0] * len(nums)

        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = max(nums[i], result[i-1] + nums[i])

        return max(result)
