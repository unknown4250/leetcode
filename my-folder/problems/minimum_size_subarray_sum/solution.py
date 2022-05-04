class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        left, right = 0, len(nums) + 1
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                right = min(right, i - left + 1)
                sum -= nums[left]
                left += 1
        return right if right != len(nums) + 1 else  0