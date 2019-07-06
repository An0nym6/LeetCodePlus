class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        position = {}
        left = 0
        right = 0
        ans = 1
        while right < len(s):
            if s[right] in position and not position[s[right]] is None:
                for i in range(left, position[s[right]]):
                    position[s[i]] = None
                left = position[s[right]] + 1
            position[s[right]] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans
