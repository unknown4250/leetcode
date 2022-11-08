class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(image[0]), len(image)

        # 픽셀 방문 표시
        visited = [[False]*m for _ in range(n)]

        queue = deque()

        # 시작점을 큐에 삽입
        queue.append((sr, sc))

        # 시작점의 색
        start_color = image[sr][sc]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while queue:
            # 탐색할 픽셀
            cur_x, cur_y = queue.popleft()

            # color로 픽셀 값 변경
            image[cur_x][cur_y] = color
            # 해당 위치의 픽셀 방문 표시
            visited[cur_x][cur_y] = True

            for i in range(4):
                # 현재 위치의 상하좌우 탐색
                nx, ny = cur_x + dx[i], cur_y + dy[i]

                # 범위를 벗어나지 않으면서 시작점의 색깔과 같은 픽셀
                if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == start_color:
                    # 방문하지 않은 픽셀이라면 큐에 삽입
                    if not visited[nx][ny]:
                        queue.append((nx, ny))

        return image

        