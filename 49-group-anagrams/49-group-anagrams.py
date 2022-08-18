from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        
        return list(anagrams.values())
            