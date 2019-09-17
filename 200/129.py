# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search(self, node):
        if node:
            self.currentNum *= 10
            self.currentNum += node.val
            if (not node.left) and (not node.right):
                self.ans += self.currentNum
            else:
                self.search(node.left)
                self.search(node.right)
            self.currentNum -= node.val
            self.currentNum /= 10
      
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.currentNum = 0
        self.search(root)
        return self.ans