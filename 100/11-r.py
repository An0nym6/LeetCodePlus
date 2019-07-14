# Proof by contradiction:
# https://leetcode.com/problems/container-with-most-water/discuss/175274/Formal-proof-of-the-O(n)-algorithm

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        i = 0
        j = len(height) - 1
        while (i != j):
            current = min(height[i], height[j]) * (j - i)
            if current > ans:
                ans = current
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
