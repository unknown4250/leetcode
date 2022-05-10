class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = grid
    
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = (grid[i][j])
                    continue
                elif i == 0 and j != 0:
                    dp[i][j] = (dp[i][j-1] + grid[i][j])
                elif j == 0 and i != 0:
                    dp[i][j] = (dp[i-1][j] + grid[i][j])
                else:
                    dp[i][j] = (min(dp[i][j-1], dp[i-1][j]) + grid[i][j])

        return dp[row-1][col-1]