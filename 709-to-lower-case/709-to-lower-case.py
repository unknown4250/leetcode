class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s.lower()
        return "".join(chr(ord(c) - ord('A') + ord('a')) if c >= 'A' and c <= 'Z' else c for c in s)