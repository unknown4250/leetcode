class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = collections.defaultdict(list)
        
        # 어휘순 정렬 후, 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        
        def dfs(a):
            # 어휘 순으로 방문하기 때문에 첫 번째 값 읽어야 함
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
        
        dfs('JFK')
        
        # 다시 뒤집어서 방문 순으로
        return route[::-1]