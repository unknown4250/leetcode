class Solution(object):
    def checkIfExist(self, arr):
        if 0 in arr and arr.count(0) > 1:
            return True

        for i in range(len(arr)):
            if 2 * arr[i] in arr and arr[i] != 0:
                return True
            elif arr[i] % 2 == 0 and arr[i] / 2 in arr and arr[i] != 0:
                return True
        return False