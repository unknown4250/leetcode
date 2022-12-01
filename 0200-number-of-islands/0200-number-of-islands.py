class Solution(object):
    """
    # DFS 버전
    def numIslands(self, grid):
        answer = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    answer += 1
        return answer

    def dfs(self, grid, x, y):
        # 입력 배열 범위를 벗어나는 경우, dfs 수행 X
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        
        # 섬이 아닌 경우, dfs 수행 X
        if grid[x][y] != "1":
            return

        # 해당 위치를 재탐색하지 않기 위해 "1" → "0"으로 값 변경
        grid[x][y] = "0"

        # 현재 위치에서 상하좌우를 탐색
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            self.dfs(grid, nx, ny)
    """
    def numIslands(self, grid):

        # bfs 수행하기 위한 큐 선언
        queue = deque()

        answer = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 섬인 위치만 탐색
                if grid[i][j] == "1":
                    # 다시 탐색하지 않기 위해 다른 값으로 변경
                    grid[i][j] = "0"

                     # 한 섬의 시작점
                    queue.append((i,j))

                    while queue:
                        # 현재 위치
                        x, y = queue.popleft()

                        # 현재 위치를 중심으로 상하좌우 탐색
                        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nx, ny = x+dx, y+dy

                             # 그리드 영역 벗어나는 경우 제외
                            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                                continue
                            
                            # 새로운 위치가 섬인 경우
                            if grid[nx][ny] == "1":
                                # 이후에 탐색할 위치
                                queue.append((nx, ny))

                                # 방문 표시
                                grid[nx][ny] = "0"
                                
                    # while문 종료되면 하나의 섬 탐색이 종료된 것 (섬 개수 +1)
                    answer += 1

        return answer