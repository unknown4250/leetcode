class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0, 0, 0] + nums

        for i in range(3, len(nums)):
            nums[i] = max(nums[i-3]+nums[i], nums[i-2]+nums[i])
        return max(nums)