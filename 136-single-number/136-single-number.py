class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        counter_dict = Counter(nums)
        for key, val in counter_dict.items():
            if val == 1:
                return key