class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = []
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            # person[1]을 인덱스로 사용해서 추출
            # insert(i, x): 위치 i에 x 값 삽입 
            result.insert(person[1], [-person[0], person[1]])
        return result