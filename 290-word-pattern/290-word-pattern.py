class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}

        lst = s.split()
        
        if len(pattern) != len(lst):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in dict1:
                if lst[i] not in dict2:
                    dict1[pattern[i]] = lst[i]
                    dict2[lst[i]] = pattern[i]
                else:
                    return False
            else:
                if dict1[pattern[i]] != lst[i]:
                    return False
        return True