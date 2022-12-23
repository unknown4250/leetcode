class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        
        info = {i: set() for i in range(numCourses)}

        graph = defaultdict(set)

        for a, b in prerequisites:
            # 전제 조건 저장 (b를 수강해야 a 수강 가능)
            info[a].add(b)

            # 수업 간 연결 정보 저장
            graph[b].add(a)
        
        queue = deque([])

        # 시작점 찾기
        for k, v in info.items():
            # 전제 조건이 없는 수업이라면, 시작점이 될 수 있음
            if len(v) == 0:
                queue.append(k)

        # 수강 순서
        path = []

        # bfs 탐색
        while queue:
            course = queue.popleft()
            
            # 해당 수업을 수강 순서에 추가
            path.append(course)

            # 모든 수업을 수강했다면 탐색 종료
            if len(path) == numCourses:
                return path
            
            # 연결된 수업 탐색
            for c in graph[course]:
                # 현재 수강한 수업이 연결된 수업의 전제 조건이라면 제거 (수강했으므로 전제 조건 사라짐)
                info[c].remove(course)

                # 전제 조건이 없는 수업이라면 탐색 타겟이 됨
                if not info[c]:
                    queue.append(c)
        
        return []