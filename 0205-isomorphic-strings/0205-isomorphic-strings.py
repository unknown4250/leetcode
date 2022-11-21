class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}

        # key: 문자, value: 문자의 위치
        for i, val in enumerate(s):
            dict1[val] = dict1.get(val, []) + [i]

        for i, val in enumerate(t):
            dict2[val] = dict2.get(val, []) + [i]
        
        # 각 문자들의 위치 구조가 동일한지 확인
        return sorted(dict1.values()) == sorted(dict2.values())
        