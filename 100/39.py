class Solution(object):
    def search(self, ans, target, selected):
        for element in self.all:
            if target == element:
                ans.add(tuple(sorted(selected + [element])))
            elif target > element:
                self.search(ans, target - element, selected + [element])                

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = set([])
        self.all = candidates
        self.search(ans, target, [])
        return ans
