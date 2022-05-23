class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)

        for i, x in enumerate(nums[:-2]):
            # Sum of any two sides should be greater than the third side.
            # Consider sides: A[i], A[i+1] and A[i+2] 
            # A[i] >= A[i+1] >= A[i+2] since the list is sorted
            # A[i] >= A[i+1] so A[i] + A[i+2] > A[i+1] and also A[i] >= A[i+2] so A[i] + A[i+1] > A[i+2] hence
            # the only condition we need to check is that A[i] < A[i+1] + A[i+2] 
            if x < nums[i+1] + nums[i+2]:
                return x + nums[i+1] + nums[i+2]

            # Another thing to note here is that: we have reached this point that means, A[i] > A[i+1] + A[i+2]
            # So there is no way that A[i] < A[i+1] and A[j] where j > i+2 so we need not consider all permutations
            # of A[i], A[i+1], A[i+3] or A[i], A[i+1], A[i+4] and so on.

            # Hence the next case to be considered would be A[i+1], A[i+2] and A[i+3]
            # hence just incrementing i would do the job
            
        return 0
