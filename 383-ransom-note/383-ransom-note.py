from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        ransom_note_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)

        for ch in ransom_note_counts.keys():
            if ransom_note_counts[ch] > magazine_counts[ch]:
                return False
        return True
