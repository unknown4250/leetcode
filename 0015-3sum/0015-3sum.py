class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        # 오름차순 정렬
        nums.sort()

        # 최소 값(nums[i])은 고정하고 합이 0이 되는 나머지 두 숫자 찾기
        # 투-포인터 방식
        for i in range(len(nums) - 2):
            
            # 양수 나오면 그 이후는 체크할 필요 없음
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 왼쪽, 오른쪽 포인터
            left, right = i + 1, len(nums) - 1

            while left < right:
                # 세 수의 합
                sum = nums[i] + nums[left] + nums[right]
                # 합이 0보다 크면, 가장 큰 값 변경
                if sum > 0:
                    right -= 1
                # 합이 0보다 작으면, 가장 작은 값 변경
                elif sum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # left와 right 인덱스 이동(중복된 값은 무시)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return res