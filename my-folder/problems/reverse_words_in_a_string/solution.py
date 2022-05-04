class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        reversed_str = list(reversed(s.split()))
        result = ' '.join(reversed_str)

        return result
