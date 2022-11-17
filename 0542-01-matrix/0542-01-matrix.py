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
                # 값이 0인 셀을 기준으로 탐색 시작
                if mat[i][j] == 0:
                    queue.append((0, i, j)) # 큐에 삽입 (거리, y좌표, x좌표)
                    visited[i][j] = True    # 방문 표시


        while queue:
            distance, x, y = queue.popleft()
            distance += 1

            # 현재 셀의 상하좌우 탐색
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy

                # 행렬 범위 벗어나면 제외
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                
                # 방문하지 않은 셀인 경우
                if not visited[nx][ny]:
                    # 현재 셀의 방문 표시
                    visited[nx][ny] = True
                    # 이후에 현재 셀의 주변을 탐색하기 위해 큐에 삽입
                    queue.append((distance, nx, ny))
                    # 0으로부터의 행렬에 직접 입력
                    mat[nx][ny] = distance

        return mat