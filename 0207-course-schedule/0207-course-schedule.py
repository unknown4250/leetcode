class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)

        # 강의 정보 입력
        for a, b in prerequisites:
            graph[a].append(b)
        
        # 순환 여부, 방문 여부 확인하기 위한 set
        traced, visited = set(), set()
                
        def dfs(node):
            # 방문 내역에 남아있으면 순환구조
            if node in traced:
                return False

            # 이미 방문한 노드라면 제외(가지치기)
            if node in visited:
                return True

            # 현재 노드를 방문 내역에 추가
            traced.add(node)

            # 현재 강의의 선행 강의들의 DFS 수행
            for course in graph[node]:
                if not dfs(course):
                    return False
            
            # 제거하지 않으면 같은 선행 강의를 갖는 다른 강의가 순환 구조로 판단될 수 있음
            traced.remove(node)
            
            # 방문 표시
            visited.add(node)

            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True