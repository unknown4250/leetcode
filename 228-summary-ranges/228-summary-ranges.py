class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)

        i = 0
        while i < n:
            start = i
            end = start + 1

            # 연속된 수의 범위 찾기
            while end < n:
                if nums[start] + 1 == nums[end]:
                    start += 1
                    end += 1
                else:
                    break

            if i != end-1:
                res.append("%d->%d" % (nums[i], nums[end-1]))
            else:
                res.append(str(nums[i]))

            # 연속된 수 이후부터 다시 탐색
            i = end
        return res

        