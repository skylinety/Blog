#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def traversal(root):
            if not root:
                return
            if root.left:
                 traversal(root.left)
            ret.append(root.val)
            if root.right:
                 traversal(root.right)
        traversal(root)
        return ret
# @lc code=end

