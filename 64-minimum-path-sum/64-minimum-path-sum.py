class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    grid[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    grid[i][j] += grid[i][j-1]
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[row-1][col-1]