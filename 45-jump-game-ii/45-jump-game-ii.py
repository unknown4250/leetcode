class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = r = cnt = 0
        
        while r < len(nums) - 1:
            cnt += 1
            next_loc = max([i + nums[i] for i in range(l, r + 1)])
            l, r = r + 1, next_loc
        
        return cnt