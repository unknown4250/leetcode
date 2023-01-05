class Solution(object):
    def maxAreaOfIsland(self, grid):
        # 그리드의 세로, 가로 길이
        m, n = len(grid), len(grid[0])

        # 방문 여부 표시할 배열
        visited = [[False] * n for _ in range(m)]

        # 섬의 최대 면적 초기화
        max_area = 0

        # bfs를 위한 큐 선언
        queue = deque([])

        for i in range(m):
            for j in range(n):
                # 현재 탐색하고 있는 섬의 면적 초기화
                temp_area = 0

                # 방문하지 않은 땅인 경우
                if grid[i][j] and not visited[i][j]:
                    # 탐색하기 위해 큐에 삽입
                    queue.append((i, j))

                    # 큐가 끝날 때까지 탐색 반복
                    while queue:

                        # 섬에서의 현재 위치
                        x, y = queue.popleft()
                        
                        # 방문했던 적 있으면 탐색 건너뜀
                        if visited[x][y]:
                            continue

                        # 방문 표시
                        visited[x][y] = True

                        # while문 한번 돌때마다 섬의 면적 증가
                        temp_area += 1

                        # 상하좌우 탐색
                        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nx = x + dx
                            ny = y + dy

                            # 그리드의 범위 벗어나면 탐색 건너뜀
                            if nx >= m or nx < 0 or ny >= n or ny < 0:
                                continue
                            
                            # 인접한 위치가 방문하지 않은 땅인 경우
                            if grid[nx][ny] and not visited[nx][ny]:
                                # 다음 탐색 대상이 됨
                                queue.append((nx, ny))

                # 현재 섬 면적과 최대 면적 비교                
                max_area = max(temp_area, max_area)

        return max_area