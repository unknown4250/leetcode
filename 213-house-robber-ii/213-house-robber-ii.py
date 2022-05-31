class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def helper(nums):
            dp = [0] * len(nums)
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            return max(dp)
        
        if len(nums) < 3:
            return max(nums)
            
        return max(helper(nums[1:]), helper(nums[:-1]))