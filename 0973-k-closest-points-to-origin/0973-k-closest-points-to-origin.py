class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        heap = []
        for point in points:
            # 유클리디안 거리 계산
            distance = point[0]**2 + point[1]**2

            # (0,0)으로부터의 거리와 점의 좌표를 힙에 삽입
            heapq.heappush(heap, (distance, point))
        
        n = 1
        result = []

        while n <= k:
            # 거리가 가까운 순부터 힙에서 제거
            dist, new_point = heapq.heappop(heap)
            # 결과 배열에 추가
            result.append(new_point)
            n += 1

        return result