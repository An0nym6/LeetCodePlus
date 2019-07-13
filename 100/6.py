class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = ""
        diff = 2 * (numRows - 1)
        # Row 1
        for j in range(0, len(s), diff):
            ans += s[j]
        # Row 2 to row n - 1
        for i in range(1, numRows - 1):
            diff_ = 2 * (numRows - i - 1)
            for j in range(i, len(s), diff):
                ans += s[j]
                if j + diff_ < len(s):
                    ans += s[j + diff_]
        # Row n
        for j in range(numRows - 1, len(s), diff):
            ans += s[j]
        return ans
