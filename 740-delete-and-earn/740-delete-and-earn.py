class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        points, prev, curr = Counter(nums), 0, 0

        for val in range(max(points.keys()) + 1):
            prev, curr = curr, max(prev + points[val] * val, curr)
            print(prev, curr)
        return curr