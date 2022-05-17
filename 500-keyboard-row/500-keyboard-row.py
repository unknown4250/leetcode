class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
    
        row0 = set("qwertyuiop")
        row1 = set("asdfghjkl")
        row2 = set("zxcvbnm")

        res = []
        for word in words:
            set_word = set(word.lower())

            if set_word & row0 == set_word or set_word & row1 == set_word or set_word & row2 == set_word:
                res.append(word)
        return res