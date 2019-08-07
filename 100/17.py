class Solution(object):
    def constructStr(self, index, currentStr):
        if index == len(self.digits):
            return self.ans.append(currentStr)
        for letter in self.mapping[int(self.digits[index])]:
            self.constructStr(index + 1, currentStr + letter)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
          return []
        self.digits = digits
        self.ans = []
        self.mapping = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'],
                        ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                        ['p', 'q', 'r', 's'], ['t', 'u', 'v'],
                        ['w', 'x', 'y', 'z']]
        self.constructStr(0, "")
        return self.ans
