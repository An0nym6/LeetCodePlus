class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        # Find pivot
        start = 0
        end = len(nums) - 1
        while start != end:
            middle = (start + end) / 2
            if nums[middle] >= nums[start] and nums[middle] >= nums[end]:
                start = middle + 1
            else:
                end = middle
        pivot = start
        # Find target
        if target >= nums[0] and target <= nums[-1]:
            start = 0
            end = len(nums) - 1
        elif target >= nums[0]:
            start = 0
            end = pivot
        else:
            start = pivot
            end = len(nums) - 1
        while start != end:
            middle = (start + end) / 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                start = middle + 1
            else:
                end = middle
        return -1 if nums[start] != target else start
