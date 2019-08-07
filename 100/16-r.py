# It looks like we need 3 layers of loops, but we can combine looping start and
# end into 1 loop so we only need 2

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        minimum = -1
        for current in range(1, len(nums) - 1):
            start = 0
            end = len(nums) - 1
            while start < current and end > current:
                sumVal = nums[start] + nums[current] + nums[end]
                diff = abs(sumVal - target)
                if minimum == -1 or diff < minimum:
                    minimum = diff
                    ans = sumVal
                if sumVal > target:
                    end -= 1
                else:
                    start += 1
        return ans
