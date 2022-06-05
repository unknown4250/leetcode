class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        max_score, max_prev = 0, values[0]

        for i in range(1, len(values)):
            max_score = max(max_score, max_prev + values[i] - i)
            max_prev = max(max_prev, values[i] + i)
        return max_score
        