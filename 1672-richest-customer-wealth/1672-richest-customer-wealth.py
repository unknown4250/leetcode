class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        max = -1
        for n in accounts:
            wealth = sum(n)
            if max < wealth:
                max = wealth
                
        return max