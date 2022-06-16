class Solution(object):
    def findRelativeRanks(self, score):

        sorted_score = {num: i + 1 for i, num in enumerate(sorted(score, reverse=True))}
        
        for i in range(len(score)):
            if sorted_score[score[i]] == 1:
                score[i] = "Gold Medal"
            elif sorted_score[score[i]] == 2:
                score[i] = "Silver Medal"
            elif sorted_score[score[i]] == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(sorted_score[score[i]])
        return score