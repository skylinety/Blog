#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def inPath(root, sum):
            if root is None:
                return False

            sum += root.val

            if root.left is None and root.right is None:
                return sum == targetSum
            left = inPath(root.left, sum)
            right = inPath(root.right, sum)
            return left or right

        return inPath(root, 0)
        # def inPath(root, sum, arr):
        #     if root is None:
        #         return []

        #     sum += root.val
        #     arr += [root.val]

        #     if root.left is None and root.right is None:
        #         return arr if sum == targetSum else []
        #     left = inPath(root.left, sum, arr)
        #     right = inPath(root.right, sum, arr)
        #     return left if len(left) > 0 else right

        # return inPath(root, 0, [])

# @lc code=end
