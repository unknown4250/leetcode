
class Solution(object):
    def findAnagrams(self, s, p):
        
        answer = []
        
        counter_p = Counter(p)          # p의 문자 개수
        counter_s = Counter(s[:len(p)]) # s의 첫 글자부터 p 길이까지의 문자 개수
        
        # p의 인덱스 포인터
        i = 0
        
        # s의 인덱스 포인터
        j = len(p)

        while j <= len(s):
            # p의 문자 개수와 현재 위치에서의 p 길이까지의 문자 개수가 같으면 anagram
            if counter_p == counter_s:
                answer.append(i)
            
            # 현재 위치의 문자 개수 차감
            counter_s[s[i]] -= 1

            # 해당 문자가 카운터에서 0 이하의 값이면, 카운터에서 제거
            if counter_s[s[i]] <= 0:
                counter_s.pop(s[i])
            
            # s의 다음 문자를 카운터에 추가
            if j < len(s):
                counter_s[s[j]] += 1
            
            i += 1
            j += 1

        return answer           