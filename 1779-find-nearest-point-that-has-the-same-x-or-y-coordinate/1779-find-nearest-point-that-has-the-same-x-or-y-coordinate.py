class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        smallest_idx = -1
        smallest_dist = float("inf")
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                temp_dist = abs(x-points[i][0]) + abs(y-points[i][1]) 
                if temp_dist < smallest_dist:
                    smallest_dist, smallest_idx = temp_dist, i
        
        return smallest_idx