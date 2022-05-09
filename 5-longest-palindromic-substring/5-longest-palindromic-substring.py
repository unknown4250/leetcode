class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1: return s

        start, length = 0, 0

        for end in range(len(s)):
            # 기존 Palindromic Substring에 end포인트의 문자를 포함해도 Palindrome했을 때, 조건 만족
            # Ex. aa(a)
            if s[end-length:end+1] == s[end-length:end+1][::-1]:
                start, length = end-length, length + 1
            # 기존 Palindromic Substring에 end포인트의 문자와 Substring의 앞의 문자를 포함해도 Palindrome
            # Ex. (b)aaa(b)
            elif end - length >= 1 and s[end-length-1:end+1] == s[end-length-1:end+1][::-1]:
                start, length = end - length - 1, length + 2

        return s[start:start+length]