class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        # 이진 검색 사용
        result = set()
        nums2.sort()

        for n1 in nums1:
            i2 = bisect_left(nums2, n1)

            if len(nums2) > 0 and len(nums2) > i2 and nums2[i2] == n1:
                result.add(n1)

        return list(result)
        """
        # 투 포인터 사용
        result = set()

        nums1.sort()
        nums2.sort()

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return list(result)
