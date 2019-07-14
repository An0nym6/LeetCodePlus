class Solution(object):
    def _isMatch(self, i, j):
        # End conditions
        if i == len(self.string) and j == len(self.pattern):
            return True
        elif i == len(self.string) or j == len(self.pattern):
            return False
        # Cached conditions
        if self.table[i][j] != -1:
            return self.table[i][j]
        # Match
        if self.string[i] == self.pattern[j][0] or self.pattern[j][0] == ".":
            # Exact match
            if len(self.pattern[j]) == 1:
                self.table[i][j] = self._isMatch(i + 1, j + 1)
            # Star match
            else:
                self.table[i][j] = (self._isMatch(i + 1, j + 1) or 
                                    self._isMatch(i + 1, j) or
                                    self._isMatch(i, j + 1))
        # Not match
        else:
            # Exact match
            if len(self.pattern[j]) == 1:
                self.table[i][j] = False
            # Star match
            else:
                self.table[i][j] = self._isMatch(i, j + 1)
        return self.table[i][j]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s += "$"
        p += "$"
        # Parse pattern
        self.pattern = []
        index = 0
        while index < len(p):
            if index + 1 < len(p) and p[index + 1] == "*":
                self.pattern.append(p[index:index + 2])
                index += 2
            else:
                self.pattern.append(p[index])
                index += 1
        # Use dynamic programming to check if they match
        self.string = s
        self.table = []
        for i in range(len(self.string)):
            self.table.append([-1] * len(self.pattern))
        return self._isMatch(0, 0)
