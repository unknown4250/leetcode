class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # 0: red, 1: white, 2: blue
        idx, red, blue = 0, 0, len(nums)-1

        while idx <= blue:
            # 원소가 0인 경우
            if nums[idx] == 0:
                # 현재 값과 red 포인터 값 swap
                nums[idx], nums[red] = nums[red], nums[idx]
                # 다음 원소 탐색하기 위해 인덱스 포인터 증가
                idx += 1
                # red의 위치에 0이 왔으므로 포인터를 오른쪽으로 이동
                red += 1

            # 원소가 1인 경우
            elif nums[idx] == 1:
                # swap하지 않고 다음 원소 탐색
                idx += 1

            # 원소가 2인 경우
            else:
                # 현재 값과 blue 포인터 값 swap
                nums[idx], nums[blue] = nums[blue], nums[idx]
                # blue가 가리키던 위치에 2가 왔으므로 포인터를 왼쪽으로 이동
                blue -= 1
        