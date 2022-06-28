class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False

        num = str(x)
        n = len(num)
        l, r = 0, n - 1

        while l < r and l <= n // 2 and r >= n // 2:
            if num[l] != num[r]:
                return False
            l += 1
            r -= 1
        return True