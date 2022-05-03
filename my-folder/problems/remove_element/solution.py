class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        cnt = 0

        for num in nums:
            if num != val:
                nums[cnt] = num
                cnt += 1
        return cnt