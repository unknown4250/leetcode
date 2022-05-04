class Solution(object):
    def containsDuplicate(self, nums):
        counter = set()

        for num in nums:
            if num in counter:
                return True
            else:
                counter.add(num)
        return False
