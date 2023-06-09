# @before-stub-for-debug-begin
from python3problem102 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []
    #     ret = []
    #     def traversal(preLevel):
    #         level = []
    #         cells = []
    #         for node in preLevel:
    #             cells.append(node.val)
    #             if node.left:
    #                 level.append(node.left)
    #             if node.right:
    #                 level.append(node.right)
    #         ret.append(cells)
    #         if len(level):
    #             traversal(level)
    #     traversal([root])
    #     return ret
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []
    #     ret = []
    #     level = [root]
    #     while len(level):
    #         cells = []
    #         preLevel = level
    #         level = []
    #         for node in preLevel:
    #             cells.append(node.val)
    #             if node.left:
    #                 level.append(node.left)
    #             if node.right:
    #                 level.append(node.right)
    #         ret.append(cells)
    #     return ret
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret = []
        level = [root]
        while len(level):
            cells = []
            # len(level)一开始为固定值
            for _ in range(len(level)):
                node = level.pop(0)
                cells.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ret.append(cells)
        return ret
# @lc code=end


