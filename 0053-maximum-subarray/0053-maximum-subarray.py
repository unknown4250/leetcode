class Solution(object):
    def maxSubArray(self, nums):
        # 서브 배열의 최대 합을 저장할 배열
        sums = [0] * len(nums)

        # 배열 첫 번째 요소 초기화
        sums[0] = nums[0]

        # 입력 배열의 현재 값과, 이전까지의 합을 비교
        for i in range(1, len(nums)):
            sums[i] = max(nums[i], sums[i-1]+nums[i])
        
        return max(sums)
