class Solution(object):
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])

        visited = [[False] * n for _ in range(m)]
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited[i][j] = True

        while queue:
            for _ in range(len(queue)):
                x, y, dist = queue.popleft()

                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue

                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist+1))
                        mat[nx][ny] = dist+1

        
        return mat
        