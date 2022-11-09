class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        counter = {}
        
        for ch in ransomNote:
            if ch in counter:
                counter[ch] += 1
            else:
                counter[ch] = 1
        

        for ch in magazine:
            if ch in counter:
                counter[ch] -= 1        

        for k, v in counter.items():
            if counter[k] > 0:
                return False
            
        return True