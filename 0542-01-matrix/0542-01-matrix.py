class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = deque()
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # 값이 0인 셀을 기준으로 탐색 시작
                if mat[i][j] == 0:
                    queue.append((i, j))  # 큐에 삽입
                    visited[i][j] = True # 방문 표시
        
        depth = 0

        while queue:
            # 0으로부터의 거리를 계산하기 위해 큐의 길이만큼 탐색하는 것을 반복
            for _ in range(len(queue)):
                x, y = queue.popleft()

                # 현재 셀의 상하좌우
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 행렬 범위 벗어나면 제외
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue

                    # 방문했던 위치라면 탐색 제외
                    if visited[nx][ny]:
                        continue

                    queue.append((nx, ny)) # 다음 탐색 대상
                    visited[nx][ny] = True # 방문 표시

                # 0이 아니면 거리 계산
                if mat[x][y] != 0:
                    mat[x][y] = mat[x][y] + depth - 1

            # 현재 depth의 모든 숫자를 탐색했으므로 depth 증가
            depth += 1

        return mat