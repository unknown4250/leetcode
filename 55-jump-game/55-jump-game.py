class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        

        len_nums = len(nums) - 1

        for i in range(len_nums, -1, -1):
            if i + nums[i] >= len_nums:
                len_nums = i

        return True if len_nums == 0 else False