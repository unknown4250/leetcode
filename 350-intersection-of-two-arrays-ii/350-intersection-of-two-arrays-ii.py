class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 공통된 중복값도 모두 처리해야 하므로 일반적인 교집합과는 다름
        # 값이 몇 개 들어있는지 알 수 있어야 중복을 제거하지 않고 처리할 수 있음
        # 따라서 Counter를 사용해서 배열의 원소 값 개수를 카운트하는 딕셔너리 필요
        counter = Counter(nums1)

        result = []
        for num in nums2:
            if num in counter.keys() and counter[num] > 0:
                counter[num] -= 1
                result.append(num)
        return result