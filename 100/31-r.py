# Inversely search through the list, find the first descending element, reverse
# the list after that element, and swap this element with the next larger
# element behind it

class Solution(object):
    def reverse(self, nums, start, end):
        if start < end:
            for i in range(start, int((end - start) / 2 + start + 1)):
                temp = nums[i]
                nums[i] = nums[end - (i - start)]
                nums[end - (i - start)] = temp

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        last = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < last:
                self.reverse(nums, i + 1, len(nums) - 1)
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        break
                return
            last = nums[i]
        self.reverse(nums, 0, len(nums) - 1)
