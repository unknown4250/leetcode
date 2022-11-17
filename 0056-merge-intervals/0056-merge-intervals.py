class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # 구간의 시작을 기준으로 오름차순 정렬
        intervals.sort(key=lambda x:(x[0]))
        
        # 첫 번째 구간을 결과 배열에 저장
        answer = [intervals[0]]

        for i in range(1, len(intervals)):
            # 구간의 시작점이 배열에 저장된 마지막 구간의 끝점보다 같거나 작은 경우
            if intervals[i][0] <= answer[-1][1]:
                # 구간의 끝점을 두 구간의 끝점 중 최대값으로 변경
                answer[-1][1] = max(intervals[i][1], answer[-1][1])
            # 구간의 시작점이 배열 마지막 구간의 끝점보다 크면 그대로 배열에 추가
            else:
                answer.append(intervals[i])
        
        return answer