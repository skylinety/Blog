#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root):
            if not root:
                return 0
            leftDepth = getDepth(root.left)
            rightDepth = getDepth(root.right)
            if leftDepth == -1 or rightDepth == -1 or abs(leftDepth - rightDepth) > 1:
                return -1
            return max(leftDepth, rightDepth) + 1
        return getDepth(root) > -1

        # def getDepth(root):
        #     if not root:
        #         return 0
        #     return max(getDepth(root.left), getDepth(root.right)) + 1

        # if not root:
        #     return True
        # return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(getDepth(root.left) - getDepth(root.right)) < 2

        # def getDepth(root):
        #     if not root:
        #         return 0
        #     return max(getDepth(root.left), getDepth(root.right)) + 1

        # if not root:
        #     return True
        # if root.left is None or root.right is None:
        #     if root.left:
        #         return root.left.left is None and root.left.right is None
        #     if root.right:
        #         return root.right.left is None and root.right.right is None
        #     return True

        # return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(getDepth(root.left) - getDepth(root.right)) < 2

# @lc code=end
