class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        # 인접 리스트 그래프 구성
        for u, v, w in times:
            graph[u].append((v, w))
            
        # 큐 : [(소요시간, 정점)]
        priority_queue = [(0, k)]
        
        dist = collections.defaultdict(list)
        
        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while priority_queue:
            time, node = heapq.heappop(priority_queue)
            
            if not node in dist:
                dist[node] = time
                
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(priority_queue, (alt, v))
                    
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        
        return -1