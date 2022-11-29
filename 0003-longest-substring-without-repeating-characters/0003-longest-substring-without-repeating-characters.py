class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # 각 문자가 나타난 마지막 위치 저장
        used = {}

        # 중복 없는 문자열의 시작 인덱스, 최대 길이 저장할 변수
        start_idx, max_length = 0, 0

        for idx, ch in enumerate(s):
            # 중복된 문자이면서 문자열의 시작 위치가 기존 문자의 위치보다 이전일 경우
            if ch in used and start_idx <= used[ch]:

                # 새로 탐색을 시작할 위치를 이전에 나온 중복된 문자 다음으로 변경
                # abcade -> 2번째 a가 나오는 경우 start_idx는 'b'의 위치로 업데이트 
                start_idx = used[ch] + 1
            
            else:
                # 최대 문자열 길이 업데이트
                max_length = max(max_length, idx - start_idx + 1)

            # 문자의 현재 위치 저장
            used[ch] = idx

        return max_length

        