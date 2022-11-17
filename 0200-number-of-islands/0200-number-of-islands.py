class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # 그리드의 세로, 가로 길이
        m, n = len(grid), len(grid[0])

        # 결과 값
        count = 0

        # bfs 수행하기 위한 큐 선언
        queue = deque([])

        for i in range(m):
            for j in range(n):
                # 섬인 위치에 대해서만 탐색
                if grid[i][j] == '1':
                    # 다시 탐색하지 않기 위해 다른 값으로 변경
                    grid[i][j] = '0'

                    # 한 섬의 시작점
                    queue.append((i, j))

                    while queue:
                        x, y = queue.popleft()

                        # 현재 위치를 중심으로 상하좌우 탐색
                        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nx = x + dx
                            ny = y + dy

                            # 그리드 영역 벗어나거나 섬이 아닌 경우 제외
                            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != '1':
                                continue
                            
                            # 이후에 탐색할 중심점 위치
                            queue.append((nx, ny))
                            
                            # 방문 표시
                            grid[nx][ny] = '0'

                    # while문 종료되면 하나의 섬 탐색이 종료된 것 (섬 개수 +1)
                    count += 1
        return count