class Solution(object):
    def threeSum(self, nums):
        res = []

        # 오름차순 정렬하는 게 좋음
        # 1. 양수 나오면 그 이후는 체크할 필요 없음
        # 2. 중복된 숫자는 인덱스만 계속 옮겨서 지나갈 수 있음
        nums.sort()

        # 최소 값(nums[i])은 고정하고 합이 0이 되는 나머지 두 숫자 찾기
        # 투-포인터 방식
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
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