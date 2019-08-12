# The key is the first missing number must be smaller than len(nums)

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rightNums = [0] * (len(nums) + 1)
        for num in nums:
            if num > 0 and num < (len(nums) + 1) and rightNums[num - 1] != num:
                rightNums[num - 1] = num
        for i in range(len(rightNums)):
            if rightNums[i] != i + 1:
                return i + 1
