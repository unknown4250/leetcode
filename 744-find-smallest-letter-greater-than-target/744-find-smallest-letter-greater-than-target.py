class Solution(object):
    def nextGreatestLetter(self, letters, target):        
        for ch in letters:
            if target < ch:
                return ch
        return letters[0]
        