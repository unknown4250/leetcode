class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        # 1. Counter 사용 버전
        counter1 = Counter()
        counter2 = Counter()
        
        # 두 입력 문자열의 길이가 다르면 False 리턴
        if len(s) != len(t):
            return False
        
        # 문자열에 속한 각 문자의 개수를 카운터에 저장
        for i in range(len(s)):
            counter1[s[i]] = counter1.get(s[i], 0) + 1
            counter2[t[i]] = counter2.get(t[i], 0) + 1
        
        # 두 카운터가 같으면 True, 다르면 False 리턴
        return True if counter1 == counter2 else False
        """
        
        # 2. 한 줄 버전
        # return sorted(s) == sorted(t)
        
        # 3. 딕셔너리로 카운터 직접 만들기
        dict = {}

        for ch in s:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1

        for ch in t:
            if ch in dict:
                dict[ch] -= 1
            else:
                return False

        for val in dict.values():
            if val != 0:
                return False
        return True
        
