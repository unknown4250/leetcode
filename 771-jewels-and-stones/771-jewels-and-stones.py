class Solution(object):
    def numJewelsInStones(self, jewels, stones):

        return sum(stones.count(ch) for ch in jewels)