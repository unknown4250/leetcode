class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m, n = len(mat), len(mat[0])
        queue = deque()

        visited = [[False] * n for _ in range(m)]


        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((0, i, j))
                    visited[i][j] = True


        while queue:
            depth, x, y = queue.popleft()

            depth += 1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((depth, nx, ny))
                    mat[nx][ny] = depth

        return mat