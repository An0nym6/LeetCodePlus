class Solution(object):
    def constructStr(self, numLeft, numRight, currentStr):
        if len(currentStr) == self.n * 2:
            return self.ans.append(currentStr)
        if numLeft < self.n:
            self.constructStr(numLeft + 1, numRight, currentStr + '(')
        if numRight < numLeft:
            self.constructStr(numLeft, numRight + 1, currentStr + ')')

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.ans = []
        self.constructStr(0, 0, "")
        return self.ans
        