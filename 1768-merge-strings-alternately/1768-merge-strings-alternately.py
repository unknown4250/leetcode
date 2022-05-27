class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        len_word1 = len(word1)
        len_word2 = len(word2)

        idx1, idx2 = 0, 0

        res = ""
        while idx1 < len_word1:
            res += word1[idx1]
            idx1 += 1
            if idx2 < len_word2:
                res += word2[idx2]
                idx2 += 1

        if idx2 < len_word2:
            res += word2[idx2:]

        return res