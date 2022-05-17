class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] not in dict_s:
                if t[i] not in dict_t:
                    dict_s[s[i]] = t[i]
                    dict_t[t[i]] = s[i]
                else:
                    return False
            else:
                if dict_s[s[i]] != t[i]:
                    return False

        return True
