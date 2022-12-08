class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        # 조합 사용한 버전
        answer = []

        for i in range(len(nums)+1):
            for combi in combinations(nums, i):
                answer.append(list(combi))

        return answer       
        """
        results = []
        
        def dfs(idx, path):
            results.append(path)
            
            # 경로 만들면서 dfs 실행
            for i in range(idx, len(nums)):
                dfs(i+1, path+[nums[i]])
        
        dfs(0, [])
        
        return results
