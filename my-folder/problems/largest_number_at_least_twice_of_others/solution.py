class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        largest_idx = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[largest_idx]:
                largest_idx = i

        for i in range(0, len(nums)):
            if nums[i] != nums[largest_idx] and nums[i]*2 > nums[largest_idx]:
                return -1

        return largest_idx
