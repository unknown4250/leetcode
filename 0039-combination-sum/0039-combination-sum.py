class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []

        def dfs(nums, target, path):
            # target이 0 미만이면 현재 path로는 target 만들 수 없음
            if target < 0:
                return
            # target이 0이 되면, path의 합이 target이 됨
            elif target == 0:
                answer.append(path)
                return
            # 재귀적으로 dfs 호출
            for i in range(len(nums)):
                dfs(nums[i:], target-nums[i], path+[nums[i]])
                

        dfs(candidates, target, [])
        return answer
        