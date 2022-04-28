class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        if arr[0] > arr[1]:
            return False

        i = 0

        while i + 1 < len(arr) and arr[i] < arr[i+1]:
            i += 1

        if i == 0 or i == len(arr) - 1:
            return False

        while i + 1 < len(arr) and arr[i] > arr[i+1]:
            i += 1

        return i == len(arr) - 1

