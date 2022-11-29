class Solution(object):
    def insert(self, intervals, newInterval):
        result = []

        new_start, new_end = newInterval[0], newInterval[1]

        for start, end in intervals:
            # 새 인터벌의 시작점이 기존 인터벌의 끝점보다 크거나
            # 새 인터벌의 끝점이 기존 인터벌의 시작점보다 큰 경우
            if end < new_start or start > new_end:
                # 겹치는 부분 없으므로 결과에 추가
                result.append([start, end])
                continue

            # 겹치는 인터벌의 시작점과 끝점 계산
            new_start = min(new_start, start)
            new_end = max(new_end, end)

        # 새로운 인터벌 결과에 추가 -> 마지막에 저장됨
        result.append([new_start, new_end])

        # 각 인터벌의 시작점을 기준으로 정렬
        return sorted(result, key=lambda x: x[0])