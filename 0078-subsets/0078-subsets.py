class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        self.dfs(nums, [], res)
        
        return res
    
    def dfs(self, numbers, path, result):
        result.append(path)
        
        for i in range(len(numbers)):
            self.dfs(numbers[i+1:], path+[numbers[i]], result)