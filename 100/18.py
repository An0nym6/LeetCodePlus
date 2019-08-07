class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = set([])
        for current1 in range(1, len(nums) - 2):
            for current2 in range(current1 + 1, len(nums) - 1):
                start = 0
                end = len(nums) - 1
                while start < current1 and end > current2:
                    sumVal = (nums[start] + nums[current1] + nums[current2] +
                              nums[end])
                    if sumVal == target:
                        ans.add(tuple(sorted((nums[start], nums[current1],
                                              nums[current2], nums[end]))))
                        start += 1
                    elif sumVal < target:
                        start += 1
                    else:
                        end -= 1
        return ans
