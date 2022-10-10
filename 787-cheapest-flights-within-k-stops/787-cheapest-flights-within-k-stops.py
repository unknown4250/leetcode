class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        my_queue = [(0, src, k+1)]
        
        # 그래프에 loop 있는 경우, time limit 발생함
        # 최소 비용으로 특정 노드에 가기까지 남아있는 횟수 기록
        visited = [False] * n
        
        while my_queue:
            price, node, stops = heapq.heappop(my_queue)
            
            if node == dst:
                return price
            
            # 이전에 방문했던 노드라면 현재 방문할 필요가 없음
            # 방문 횟수가 더 많이 남고, 비용도 더 적은 상태에서 방문했으니까
            if visited[node] >= stops:
                continue
            
            visited[node] = stops
            

            for v, w in graph[node]:
                heapq.heappush(my_queue, (price + w, v, stops-1))
        
        return -1