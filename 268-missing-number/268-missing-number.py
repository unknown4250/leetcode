class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return list(set([i for i in range(len(nums) + 1)]) - set(nums))[0]
        set_nums = set(nums)

        for i in range(len(nums) + 1):
            if i not in set_nums:
                return i