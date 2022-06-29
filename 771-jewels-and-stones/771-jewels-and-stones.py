class Solution(object):
    def numJewelsInStones(self, jewels, stones):

        res = 0
        for stone in stones:
            if stone in jewels:
                res += 1
        return res