class Solution(object):
    def search(self, ans, start, target, selected):
        if start < len(self.all):
            if self.all[start] == target:
                ans.add(tuple(selected + [self.all[start]]))
            elif self.all[start] < target:
                self.search(ans, start + 1, target, selected)
                self.search(ans, start + 1, target - self.all[start],
                            selected + [self.all[start]])

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = set([])
        self.all = sorted(candidates)
        self.search(ans, 0, target, [])
        return ans