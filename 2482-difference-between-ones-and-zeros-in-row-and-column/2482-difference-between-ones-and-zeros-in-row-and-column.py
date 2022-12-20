class Solution(object):
    def onesMinusZeros(self, grid):
        one_rows, one_cols = [0] * len(grid), [0] * len(grid[0])

        # 각 행, 열에 1이 몇 개씩 있는지 카운팅
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    one_rows[i] += 1
                    one_cols[j] += 1
        
        # 결과 배열
        diff = [[0] * len(grid[0]) for _ in range(len(grid))]

        # 1과 0의 개수 차이 계산
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = one_rows[i] + one_cols[j] - (len(grid) - one_rows[i]) - (len(grid[0]) - one_cols[j])
        
        return diff