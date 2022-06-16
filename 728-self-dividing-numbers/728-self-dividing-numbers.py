class Solution(object):
    def selfDividingNumbers(self, left, right):

        res = []

        for i in range(left, right + 1):
            temp = i

            while True:
                if temp % 10 == 0 or i % (temp % 10) != 0:
                    break
                temp //= 10
                
            if temp == 0:
                res.append(i)
                
        return res