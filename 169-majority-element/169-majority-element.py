class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for n in nums:
            dict[n] = dict.get(n, 0) + 1
            """
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
            """
            if dict[n] > len(nums) / 2:
                return n