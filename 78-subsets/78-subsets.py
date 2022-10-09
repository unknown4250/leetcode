class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def dfs(idx, path):
            results.append(path)
            
            # 경로 만들면서 dfs 실행
            for i in range(idx, len(nums)):
                dfs(i+1, path+[nums[i]])
        
        dfs(0, [])
        
        return results