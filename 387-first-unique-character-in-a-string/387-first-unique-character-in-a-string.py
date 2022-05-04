class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        char_dict = {}

        for i in range(len(s)):
            if s[i] in char_dict:
                char_dict[s[i]] += 1
            else:
                char_dict[s[i]] = 1
        #return char_dict

        for i in range(len(s)):
            if char_dict[s[i]] == 1:
                return i
        return -1