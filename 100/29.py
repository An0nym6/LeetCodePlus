class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        flag = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while dividend >= divisor:
            temp = divisor
            score = 1
            while dividend - temp > temp:
                temp += temp
                score += score
            ans += score
            dividend -= temp
        if flag == 1:
            return min(2147483647, max(-2147483648, ans))
        return min(2147483647, max(-2147483648, -ans))
