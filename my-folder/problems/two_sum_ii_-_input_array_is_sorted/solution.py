class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        # Brute-force
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        """

        # One-pass Hash Table
        hash_map = {}
        for i, num in enumerate(numbers):
            remain = target - num

            if remain in hash_map:
                return [hash_map[remain] + 1, i + 1]
            else:
                hash_map[num] = i