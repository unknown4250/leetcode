class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt = 0
        while n > 1:
            x = 0
            for i in range(1, n):
                if n % i == 0:
                    x = i
                break
            n -= x
            cnt += 1

        return False if cnt % 2 == 0 else True 