# This is a very bad problem. The neat O(n^2) solution (in the comment) won't
# pass the last two cases but a slightly-optimized solution which is also O(n^2)
# can pass

class Solution(object):
    def twoSum(self, nums, target):
        hit = set([])
        for num in nums:
            if -target - num in hit:
                self.ans.add(tuple(sorted((target, num, -target - num))))
            hit.add(num)

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = set([])
        negatives = []
        zeros = []
        positives = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                negatives = nums[:i]
                break
            if i == len(nums) - 1:
                negatives = nums[:]
        for i in range(len(negatives), len(nums)):
            if nums[i] > 0:
                zeros = nums[len(negatives):i]
                break
            if i == len(nums) - 1:
                zeros = nums[len(negatives):]
        positives = nums[len(negatives) + len(zeros):]
        # 0 0 0
        if len(zeros) >= 3:
            self.ans.add((0, 0, 0))
        # - 0 +
        if len(zeros) >= 1:
            self.twoSum(positives + negatives, 0)
        # - - +
        for num in positives:
            self.twoSum(negatives, num)
        # - + +
        for num in negatives:
            self.twoSum(positives, num)
        return self.ans
        
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ans = set([])
#         twoSum = {}
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 sumVal = nums[i] + nums[j]
#                 if sumVal in twoSum and (i, j) not in twoSum:
#                     twoSum[sumVal].append((i, j))
#                 else:
#                     twoSum[sumVal] = [(i, j)]
#         for index, num in enumerate(nums):
#             if -num in twoSum:
#                 for pair in twoSum[-num]:
#                     if index != pair[0] and index != pair[1]:
#                         ans.add(
#                             tuple(
#                                 sorted([num, nums[pair[0]], nums[pair[1]]])
#                             )
#                         )
#         return ans
