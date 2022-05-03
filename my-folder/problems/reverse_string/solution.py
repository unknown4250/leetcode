class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        

        len_str = len(s)
        for i in range(int(len_str/2)):
            s[i], s[len_str - i - 1] = s[len_str - i - 1], s[i]

        return s