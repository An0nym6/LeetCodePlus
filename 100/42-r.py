class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxLeft = []
        maxRight = []
        maximum = 0
        for h in height:
            if h > maximum:
                maximum = h
            maxLeft.append(maximum)
        maximum = 0
        for h in reversed(height):
            if h > maximum:
                maximum = h
            maxRight.append(maximum)
        ans = 0
        maxRight.reverse()
        for i, h in enumerate(height):
            ans += (min(maxLeft[i], maxRight[i]) - height[i])
        return ans