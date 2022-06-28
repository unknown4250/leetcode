class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_numerals = {1000:'M',
                          900: 'CM',
                          500: 'D',
                          400: 'CD',
                          100: 'C',
                          90: 'XC',
                          50: 'L',
                          40: 'XL',
                          10: 'X',
                          9: 'IX',
                          5: 'V',
                          4: 'IV',
                          1: 'I'}
        integer = sorted(roman_numerals.keys(), reverse=True)
        res = ''
        while num > 0:
            for roman_num in integer:
                if num - roman_num >= 0:
                    res += roman_numerals[roman_num]
                    num -= roman_num
                    break
        return res