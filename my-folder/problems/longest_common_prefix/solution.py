class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str1, str2 = max(strs), min(strs)
        i = match = 0
        
        while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
            i += 1
            match += 1
            
        return str1[:match]