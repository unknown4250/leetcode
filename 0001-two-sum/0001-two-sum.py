class Solution(object):
    def twoSum(self, nums, target):
        # key: 숫자, value: 인덱스
        pos = {num: idx for idx, num in enumerate(nums)}

        for i, n in enumerate(nums):
            # 현재 값과 더해서 타겟을 만들 수 있는 값
            rest = target - n

            # 타겟을 만들 수 있고, 그 위치가 현재 위치와 다른 숫자면 리턴
            if rest in pos and i != pos[rest]:
                return [i, pos[rest]]
        