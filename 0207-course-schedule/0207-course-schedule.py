class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)
        
        visited, traced = [False] * numCourses, [False] * numCourses

        def dfs(x):
            if traced[x]:
                return False
            
            if visited[x]:
                return True
            
            traced[x] = True

            for course in graph[x]:
                if not dfs(course):
                    return False
            
            traced[x] = False
            visited[x] = True

            return True
        
        for course in list(graph):
            if not dfs(course):
                return False
        return True