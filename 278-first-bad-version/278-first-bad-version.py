# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        
        left, right = 0, n - 1

        while left <= right:
            mid = (right + left) // 2
            
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left