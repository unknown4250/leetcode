class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        # 투 포인터 이용
        left, right = 0, len(numbers) - 1

        while True:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left+1, right+1]
        """
        # 이진 탐색(biscect 효율화 버전)
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            
            if i < len(numbers) and numbers[i] == expected:
                return [k + 1, i + 1]