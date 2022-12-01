class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        # 두 course를 시작점, 끝점으로 그래프에 추가
        for a, b in prerequisites:
            graph[a].append(b)
        
        # 방문 여부, 순환 여부 저장할 배열
        visited, traced = [False] * numCourses, [False] * numCourses

        def dfs(x):
            # 순환 구조라면 False 리턴
            if traced[x]:
                return False

            # 방문했던 노드라면 True 리턴
            if visited[x]:
                return True
            
            # 현재 course가 순환 구조인지 확인하기 위해 True 표시
            traced[x] = True

            # 연결된 course 탐색
            for course in graph[x]:
                # 순환 구조인 경우 False 리턴
                if not dfs(course):
                    return False
            
            # 순환 여부 확인이 끝났으므로 현재 course에 대해 다시 False 표시
            traced[x] = False

            # 방문 표시
            visited[x] = True

            return True
        
        # 시작 course를 기준으로 모두 dfs 탐색 수행
        for course in list(graph):
            if not dfs(course):
                return False
        return True