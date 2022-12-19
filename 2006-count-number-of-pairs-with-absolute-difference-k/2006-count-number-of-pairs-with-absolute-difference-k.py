class Solution(object):
    def countKDifference(self, nums, k):
        num_dict = {}

        # 숫자 개수를 저장하는 딕셔너리
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        count = 0
        for num in nums:
            # 차이가 k인 숫자가 있으면, 해당 개수만큼 pair 개수 증가
            if num + k in num_dict:
                count += num_dict[num+k]
        
        return count
