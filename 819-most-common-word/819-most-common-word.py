from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        words = [word for word in re.sub("[^\w]", " ", paragraph).lower().split() if word not in banned]
        
        word_counter = Counter(words)
        
        return word_counter.most_common()[0][0]