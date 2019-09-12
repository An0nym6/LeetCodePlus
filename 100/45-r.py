# There are tons of O(n^2) solutions
# The O(n) solution is implicitly a BFS solution

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        currentLimit = 0
        nextLimit = 0
        for i in range(len(nums) - 1):
            nextLimit = max(i + nums[i], nextLimit)
            if i == currentLimit:
                step += 1
                currentLimit = nextLimit
        return step
