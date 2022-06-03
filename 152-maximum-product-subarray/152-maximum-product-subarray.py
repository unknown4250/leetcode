class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums: return 0

        max_prod = prev_max = prev_min = nums[0]

        for i in range(1, len(nums)):
            curr_min = min(prev_max * nums[i], prev_min * nums[i], nums[i])
            curr_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
            # min 값을 저장하는 이유는 음수와 음수를 곱하면 양수가 나오기 때문
            # [-2, 3, -4]에서 두 수의 곱이 가장 큰 경우는 (-2)x(-4) = 8
            prev_min, prev_max = curr_min, curr_max
            max_prod = max(curr_max, max_prod)
        
        return max_prod