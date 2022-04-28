class Solution(object):
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)

        cnt = 0
        for i, height in enumerate(heights):
            if sorted_heights[i] != height:
                cnt += 1
        return cnt
