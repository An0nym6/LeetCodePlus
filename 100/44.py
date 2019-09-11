class Solution(object):
    def search(self, i, j):
        # End condition
        if i == -1 and j == -1:
            return True
        if i == -1 or j == -1:
            return False
        # Cached conditions
        if self.cached[i][j] != -1:
            return self.cached[i][j]
        # Normal conditions
        # By default no match
        self.cached[i][j] = False
        # Exact match
        if self.s[i] == self.p[j]:
            self.cached[i][j] = self.search(i - 1, j - 1)
        # ? match
        elif self.p[j] == "?":
            self.cached[i][j] = self.search(i - 1, j - 1)
        # * match
        elif self.p[j] == "*":
            self.cached[i][j] = (self.search(i - 1, j - 1) or
                                 self.search(i - 1, j) or
                                 self.search(i, j - 1))
        return self.cached[i][j]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.s = "a" + s
        self.p = "a" + p
        self.cached = []
        for i in range(len(self.s)):
            self.cached.append([-1] * len(self.p))
        return self.search(len(self.s) - 1, len(self.p) - 1)
