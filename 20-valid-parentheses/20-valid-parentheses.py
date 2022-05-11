class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {"(":")", "[":"]", "{":"}"}
        
        stack = []
        
        for i in s:
            if i in parentheses:
                stack.append(i)
            elif not stack or parentheses[stack.pop()] != i:
                return False
        return not stack