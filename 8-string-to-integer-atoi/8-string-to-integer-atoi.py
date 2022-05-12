class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        answer = ''
        s = s.strip()

        sign = {'-', '+'}

        for ch in s:
            if answer == '':
                if ch.isdigit() or ch in sign:
                    answer = ch
                else:
                    break
            else:
                if ch.isdigit():
                    answer += ch
                else:
                    break

        if answer == '' or answer in sign:
            answer = 0
        elif int(answer) < -2 ** 31:
            answer = -2 ** 31
        elif int(answer) > 2 ** 31 - 1:
            answer = 2 ** 31 - 1

        return int(answer)