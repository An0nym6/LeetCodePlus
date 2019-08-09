# Very interesting DP problem. Detailed solution can be found here:
# https://leetcode.com/problems/longest-valid-parentheses/solution/

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        cached = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    if i - 2 >= 0:
                        cached[i] = cached[i - 2] + 2
                    else:
                        cached[i] = 2
                elif (i - cached[i - 1] - 1 >= 0 and
                      s[i - cached[i - 1] - 1] == "("):
                    cached[i] = cached[i - 1] + 2
                    if i - cached[i - 1] - 2 >= 0:
                        cached[i] += cached[i - cached[i - 1] - 2]
            if cached[i] > ans:
                ans = cached[i]
        return ans
        