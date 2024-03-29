class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []
        
        def dfs(elements):
            # 리프 노드일 때(조합 결과 길이 = 입력 배열 길이) 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])
            
            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)
        # itertools 이용 풀이
        # return list(map(list, itertools.permutations(nums)))
        return results
    