class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            num = nums1[i]

            idx1 = 0
            while idx1 < len(nums2):
                if num == nums2[idx1]:
                    break
                idx1 += 1
            
            idx2 = idx1 + 1
            
            while idx2 < len(nums2):
                if nums2[idx2] > num:
                    res[i] = nums2[idx2]
                    break
                idx2 += 1
        return res