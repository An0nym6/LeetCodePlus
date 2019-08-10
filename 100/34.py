import math

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        pivot = None
        while start != end:
            middle = (start + end) / 2
            if nums[middle] == target:
                pivot = middle
                break
            elif nums[middle] > target:
                end = middle
            else:
                start = middle + 1
        if not pivot:
            if nums[start] == target:
                pivot = start
            else:
                return [-1, -1]
        ans = [-1, -1]
        # Search left
        start = 0
        end = pivot
        while start != end:
            middle = int(math.ceil((start + end) / 2.0))
            if nums[middle] == target:
                end = middle - 1
            else:
                start = middle
        if nums[start] == target:
            ans[0] = 0
        else:
            ans[0] = end + 1
        # Search right
        start = pivot
        end = len(nums) - 1
        while start != end:
            middle = (start + end) / 2
            if nums[middle] == target:
                start = middle + 1
            else:
                end = middle
        if nums[-1] == target:
            ans[1] = len(nums) - 1
        else:
            ans[1] = end - 1
        return ans
