class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
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
        
        