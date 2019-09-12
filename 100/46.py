class Solution(object):
    def search(self):
        if len(self.current) == len(self.nums):
            self.ans.append(self.current[:])
            return
        for i in range(len(self.nums)):
            if self.nums[i] not in self.current:
                self.current.append(self.nums[i])
                self.search()
                self.current.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.current = []
        self.ans = []
        self.nums = nums
        self.search()
        return self.ans