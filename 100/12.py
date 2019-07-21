class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        # M for 1000
        count = num / 1000
        ans += "M" * count
        num -= 1000 * count
        # C for 100
        count = num / 100
        if count == 9:
            ans += "CM"
        elif count >= 5:
            ans += ("D" + "C" * (count - 5))
        elif count == 4:
            ans += "CD"
        else:
            ans += ("C" * count)
        num -= 100 * count
        # X for 10
        count = num / 10
        if count == 9:
            ans += "XC"
        elif count >= 5:
            ans += ("L" + "X" * (count - 5))
        elif count == 4:
            ans += "XL"
        else:
            ans += ("X" * count)
        num -= 10 * count
        # I for 1
        count = num
        if count == 9:
            ans += "IX"
        elif count >= 5:
            ans += ("V" + "I" * (count - 5))
        elif count == 4:
            ans += "IV"
        else:
            ans += "I" * count
        return ans
