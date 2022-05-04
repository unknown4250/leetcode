class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

        for ch in s.split():
            reverse_str = list(reversed(ch))
            result.append(''.join(reverse_str))
        return ' '.join(result)
