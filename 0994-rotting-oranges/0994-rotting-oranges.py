class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 그리드의 세로, 가로
        m, n = len(grid), len(grid[0])

        # 결과값(분)
        answer = 0

        # bfs 수행하기 위한 큐 선언
        queue = deque([])

        fresh_oranges = 0

        for i in range(m):
            for j in range(n):
                # 썩은 오렌지들의 초기 위치 저장
                if grid[i][j] == 2:
                    queue.append((i, j))
                
                # 신선한 오렌지들의 초기 갯수 저장
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        # 큐가 비거나 신선한 오렌지가 없으면 탐색 중단
        while queue and fresh_oranges > 0:
            # 큐에는 같은 시간에 썩는 오렌지들의 위치 들어감
            # 따라서 큐의 길이만큼 반복해야 시간 계산 가능
            for _ in range(len(queue)):
                x, y = queue.popleft()

                # 현재 위치에서 상하좌우 탐색
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx = x + dx
                    ny = y + dy
                    
                    # 그리드 범위 벗어나거나 신선한 오렌지 아니면 제외
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != 1:
                        continue
                    
                    # 신선한 오렌지에서 상한 오렌지로 변경(1 -> 2)
                    grid[nx][ny] = 2
                    # 신선한 오렌지 개수 - 1
                    fresh_oranges -= 1
                    # 다음 탐색 대상 추가
                    queue.append((nx, ny))

            # 시간 증가
            answer += 1
        
        # 신선한 오렌지가 남아있지 않으면 시간을, 남아있다면 -1 리턴
        return answer if fresh_oranges == 0 else -1
        