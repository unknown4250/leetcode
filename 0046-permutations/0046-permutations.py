class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 결과 배열
        answer = []

        # 백트래킹 함수
        def backtracing(path=[]):
            # 입력 배열과 만들어낸 조합의 길이가 같으면 결과에 추가
            if len(path) == len(nums):
                answer.append(path[::])
            # 조합 만드는 과정
            else:
                for num in nums:
                    # 현재 만든 조합에 포함되지 않은 경우
                    if num not in path:
                        # 추가하고 계속 조합 만들어나가기
                        path.append(num)
                        backtracing(path)
                        # 이전에 넣었던 숫자 안들어가는 경우를 위해 다시 제거
                        path.pop()

        backtracing()

        return answer
        