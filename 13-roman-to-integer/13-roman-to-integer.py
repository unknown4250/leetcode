class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0

        for i in range(len(s) - 1):
            if roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                res -= roman_numerals[s[i]]     
            else:
                res += roman_numerals[s[i]]
        return res + roman_numerals[s[-1]]