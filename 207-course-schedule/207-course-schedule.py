class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        traced = set()
        visited = set()
        
        def dfs(i):
            # 순환 구조라면 False
            if i in traced:
                return False
            # 방문했던 노드라면 True
            if i in visited:
                return True
            
            traced.add(i)
            
            for course2 in graph[i]:
                if not dfs(course2):
                    return False
            
            # 탐색 종료 후, 새로운 탐색 위해서 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후, 방문 표시
            visited.add(i)
            
            return True
        
        # 순환 판별
        for course1 in list(graph):
            if not dfs(course1):
                return False
        
        return True
            