class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        traced = set()
        visited = set()
        
        def dfs(i):
            
            if i in traced:
                return False
            
            if i in visited:
                return True
            
            traced.add(i)
            
            for course2 in graph[i]:
                if not dfs(course2):
                    return False
                
            traced.remove(i)
            
            visited.add(i)
            
            return True
        
        
        for course1 in list(graph):
            if not dfs(course1):
                return False
        
        return True
            