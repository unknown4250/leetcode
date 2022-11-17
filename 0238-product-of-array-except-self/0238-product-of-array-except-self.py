class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        res = [1] * len(nums)

        # 현재 위치를 기준으로 왼쪽 값들의 누적 곱 저장
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]


        # 현재 위치의 오른쪽 값들의 누적 곱 저장
        tmp = 1
        for i in range(len(nums)-2, -1, -1):
            tmp *= nums[i+1]
            res[i] *= tmp
        
        return res
        