class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        my_queue = [(0, src, k+1)]
        
        # 그래프에 loop 있는 경우, time limit 발생함
        # 최소 비용으로 특정 노드에 가기까지 남아있는 횟수 기록
        visited = [0] * n
        
        while my_queue:
            price, node, stops = heapq.heappop(my_queue)
            
            if node == dst:
                return price
            
            if visited[node] >= stops:
                continue
            
            visited[node] = stops
            
            for v, w in graph[node]:
                heapq.heappush(my_queue, (price + w, v, stops-1))
        
        return -1