# @before-stub-for-debug-begin
from python3problem226 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if not root:
                return
            left = root.left
            right = root.right
            root.left = right
            root.right = left
            traverse(left)
            traverse(right)
        traverse(root)
        return root

# @lc code=end

