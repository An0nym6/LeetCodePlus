class Solution(object):
    def search(self):
        if len(self.current) == len(self.nums):
            realCurrent = [self.realNums[x] for x in self.current]
            self.ans.add(tuple(realCurrent))
            return
        for i in range(len(self.nums)):
            if self.nums[i] not in self.current:
                self.current.append(self.nums[i])
                self.search()
                self.current.pop()

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.current = []
        self.ans = set([])
        self.nums = range(len(nums))
        self.realNums = nums
        self.search()
        return self.ans