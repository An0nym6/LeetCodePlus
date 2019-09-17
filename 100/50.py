import math

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = math.pow(x, n)
        return max(min(ans, 2147483647), -2147483648)
