class Solution(object):
    def intersect(self, nums1, nums2):
        
        nums1, nums2 = sorted(nums1), sorted(nums2)
        idx1 = idx2 = 0
        res = []
        
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
            else:
                res.append(nums1[idx1])
                idx1, idx2 = idx1 + 1, idx2 + 1
        return res
