from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        res = 0

        num_counts = Counter(nums)

        for num in nums:
            if num + 1 in num_counts:
                res = max(res, num_counts[num] + num_counts[num+1])
        return res
