class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if s1 == s2: return True
        
        mismatched = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatched.append(i)
        
        if len(mismatched) != 2: return False

        s1 = list(s1)
        s1[mismatched[0]], s1[mismatched[1]] = s1[mismatched[1]], s1[mismatched[0]]
        
        return "".join(s1) == s2