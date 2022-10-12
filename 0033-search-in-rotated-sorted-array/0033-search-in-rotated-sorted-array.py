class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # min(), index()로 최솟값의 인덱스 찾기
        # pivot = nums.index(min(nums))

        # 이진 검색을 이용한 최솟값(=pivot) 위치 찾기
        # 최솟값의 위치 = rotation 횟수
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        pivot = left
        
        # pivot을 기준으로 target 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
            
        return -1
        