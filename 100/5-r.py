# 1. Dynamic programming on reverse string is wrong: acxyzca
# 2. Dynamic programming can be a good idea, but it's slower than simply
# looping through each pivot and search both sides
# 3. It seems than array is much faster than dict in Python

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = []
        for i in range(len(s)):
            table.append([0] * len(s))
        index = 0
        maxLen = 0
        for end in range(len(s)):
            for start in range(end + 1):
                if start == end:
                    table[start][end] = 1
                elif start == end - 1:
                    table[start][end] = 2 if s[start] == s[end] else 0
                else:
                    table[start][end] = end - start + 1 \
                        if s[start] == s[end] and table[start + 1][end - 1] \
                        else 0
                if table[start][end] > maxLen:
                    maxLen = table[start][end]
                    index = start
        return s[index:index + maxLen]
