class Solution(object):
    def letterCombinations(self, digits):
        keyboards = {
                     "2": "abc", "3": "def",
                     "4": "ghi", "5": "jkl",
                     "6": "mno", "7": "pqrs",
                     "8": "tuv", "9": "wxyz"
                    }

        answer = []

        if len(digits) == 0:
            return answer

        # dfs 함수 호출
        self.dfs(0, "", digits, keyboards, answer)

        return answer

    def dfs(self, idx, candidate, digits, mapping, result):
        # 만들어진 문자열과 digits의 길이 같으면 탐색 종료
        if idx == len(digits):
            result.append(candidate)
            return
        # digits의 숫자와 매핑되는 문자 읽어옴 
        for ch in mapping[digits[idx]]:
            # 기존 문자열에 새로운 문자 추가 후, 다시 dfs 수행
            self.dfs(idx+1, candidate + ch, digits, mapping, result)