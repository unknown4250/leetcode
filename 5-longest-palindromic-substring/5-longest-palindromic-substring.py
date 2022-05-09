class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1: return s

        start, length = 0, 0
        for end in range(len(s)):
            if s[end-length:end+1] == s[end-length:end+1][::-1]:
                start, length = end-length, length + 1
            elif end-length >= 1 and s[end-length-1:end+1] == s[end-length-1:end+1][::-1]:
                start, length = end - length - 1, length + 2
        return s[start:start+length]