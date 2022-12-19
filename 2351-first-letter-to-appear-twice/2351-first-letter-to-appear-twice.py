class Solution(object):
    def repeatedCharacter(self, s):
        
        letters = set()

        for ch in s:
            if ch in letters:
                return ch
            else:
                letters.add(ch)
        
        