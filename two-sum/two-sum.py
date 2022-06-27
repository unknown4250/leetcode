class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        # Brute force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[j] == nums[i]:
                    return [i, j]

        """
        dict = {n: i for i, n in enumerate(nums)}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict and dict[complement] != i:
                return [i, dict[complement]]